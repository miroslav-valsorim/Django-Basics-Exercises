from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models


def validate_username(value):
    is_valid = all(ch.isalnum() or ch == '_' for ch in value)

    if not is_valid:
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


class Profile(models.Model):
    MAX_USER_NAME = 15
    MIN_USER_NAME = 2

    username = models.CharField(
        max_length=MAX_USER_NAME,
        validators=[
            MinLengthValidator(MIN_USER_NAME),
            validate_username,
        ],
        blank=False,
        null=False,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
