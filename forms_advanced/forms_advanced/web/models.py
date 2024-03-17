from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_first_name(value):
    if " " in value:
        raise ValidationError("First name cannot contain spaces.")


class Person(models.Model):
    MIN_LENGTH_FIRST_NAME = 2
    MIN_LENGTH_LAST_NAME = 2

    MAX_LENGTH_FIRST_NAME = 32
    MAX_LENGTH_LAST_NAME = 32

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_FIRST_NAME),
            validate_first_name,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_LAST_NAME),
            validate_first_name,
        )
    )

    age = models.PositiveSmallIntegerField()

