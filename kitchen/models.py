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
