from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def starts_with_letter_validator(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 25
    MIN_FIRST_NAME_LENGTH = 2

    MAX_LAST_NAME_LENGTH = 35
    MIN_LAST_NAME_LENGTH = 1

    MAX_EMAIL_LENGTH = 40

    MAX_PASSWORD_LENGTH = 20
    MIN_PASSWORD_LENGTH = 8

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_FIRST_NAME_LENGTH),
            starts_with_letter_validator,
        ),
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_LAST_NAME_LENGTH),
            starts_with_letter_validator,
        ),
        blank=False,
        null=False,
    )

    email = models.EmailField(
        max_length=MAX_EMAIL_LENGTH,
        unique=True,
        blank=False,
        null=False,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        validators=(MinLengthValidator(MIN_PASSWORD_LENGTH),),
        blank=False,
        null=False,
        help_text="*Password length requirements: 8 to 20 characters",
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=18,
    )
