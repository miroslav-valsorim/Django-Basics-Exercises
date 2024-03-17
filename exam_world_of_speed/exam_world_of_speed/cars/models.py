from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from exam_world_of_speed.profiles.models import Profile

'''
car models
'''


def validate_year_range(value):
    if not (1999 <= value <= 2030):
        raise ValidationError('Year must be between 1999 and 2030!')


class Car(models.Model):
    TYPE_CHOICES = [
        ("Rally", "Rally"),
        ("Open-wheel", "Open-wheel"),
        ("Kart", "Kart"),
        ("Drag", "Drag"),
        ("Other", "Other"),
    ]

    MAX_TYPE_LENGTH = 10

    MAX_MODEL_LENGTH = 15
    MIN_MODEL_LENGTH = 1

    MIN_PRICE_VALUE = 1.0

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        choices=TYPE_CHOICES,
        blank=False,
        null=False,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        validators=(
            MinLengthValidator(MIN_MODEL_LENGTH),
        ),
        blank=False,
        null=False,
    )

    year = models.IntegerField(
        validators=(
            validate_year_range,
        ),
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        unique=True,
        error_messages={
            'unique': "This image URL is already in use! Provide a new one."
        },
        blank=False,
        null=False,
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE_VALUE),
        ),
        blank=False,
        null=False,
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
