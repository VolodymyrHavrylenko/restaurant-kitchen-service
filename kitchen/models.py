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
