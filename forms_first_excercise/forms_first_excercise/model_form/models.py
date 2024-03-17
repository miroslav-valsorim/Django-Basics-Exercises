from django.core.exceptions import ValidationError
from django.db import models


def non_empty(value):
    if " " in value:
        raise ValidationError("No empty spaces allowed")


class Person(models.Model):
    name = models.CharField(
        max_length=35,
        blank=False,
        null=False,
        validators=(
            non_empty,
        )
    )

    last_name = models.CharField(
        max_length=35,
        blank=False,
        null=False,
        validators=(
            non_empty,
        )
    )

    age = models.IntegerField(
        blank=False,
        null=False,
    )

    email = models.EmailField()

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"