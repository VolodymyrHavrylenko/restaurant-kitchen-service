from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    year_of_experience = models.PositiveSmallIntegerField(
        default=0,
        help_text="Number of years of cooking experience",
    )

    class Meta:
        ordering = ["-year_of_experience"]

    def __str__(self):
        return (f"{self.username} ({self.first_name} {self.last_name}) "
                f"- {self.year_of_experience} years of experience")


class DishType(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Type of dish",
    )

    class Meta:
        verbose_name = "Dish Type"
        verbose_name_plural = "Dish Types"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Name of the dish",
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Description of the dish",
    )
    price = models.PositiveIntegerField(
        default=0,
        help_text="Price of the dish",
    )
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.PROTECT,
        help_text="Type of dish",
        related_name="dishes",
    )
    cook = models.ManyToManyField(
        Cook,
        help_text="Cooks responsible for the dish",
        related_name="dishes",
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        help_text="Ingredients used in this dish",
        related_name="dishes",
    )
    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"
        ordering = ["name"]

    def __str__(self):
        if self.description:
            return f"{self.name} - {self.description}"
        return self.name
