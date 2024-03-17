from django.core.validators import MinValueValidator
from django.db import models

from exam_prep_one.profiles.models import Profile


class Album(models.Model):
    MAX_ALBUM_NAME_LENGTH = 30
    MAX_ARTIST_LENGTH = 30
    MAX_GENRE_LENGTH = 30

    GENRE_CHOICES = [
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'), ]

    album_name = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH,
        unique=True,
        blank=False,
        null=False,
    )

    artist = models.CharField(
        max_length=MAX_ARTIST_LENGTH,
        blank=False,
        null=False,
    )

    genre = models.CharField(
        choices=GENRE_CHOICES,
        max_length=MAX_GENRE_LENGTH,
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        validators=(MinValueValidator(0.0),),
        blank=False,
        null=False,
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
