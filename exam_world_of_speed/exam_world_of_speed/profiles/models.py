from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

'''
profile models
'''


def validate_username(value):
    is_valid = all(ch.isalnum() or ch == '_' for ch in value)

    if not is_valid:
        raise ValidationError('"Username must contain only letters, digits, and underscores!')


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15

    MIN_AGE_VALUE = 21

    MAX_PASSWORD_LENGTH = 20

    MAX_FIRST_NAME_LENGTH = 25

    MAX_LAST_NAME_LENGTH = 25

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(3, message="Username must be at least 3 chars long!"),
            validate_username,
        ),
        blank=False,
        null=False,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(MIN_AGE_VALUE),
        ),
        help_text='Age requirement: 21 years and above.',
        blank=False,
        null=False,

    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
