from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from exam_prep_two.profiles.models import Profile


def letters_only_validator(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")


class Fruits(models.Model):
    MAX_FRUIT_LENGTH = 30
    MIN_FRUIT_LENGTH = 2

    name = models.CharField(
        max_length=MAX_FRUIT_LENGTH,
        validators=(
            MinLengthValidator(MIN_FRUIT_LENGTH),
            letters_only_validator,
        ),
        unique=True,
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
