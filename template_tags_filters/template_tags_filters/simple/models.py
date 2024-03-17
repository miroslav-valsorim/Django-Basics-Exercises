from django.db import models


# Create your models here.

class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=30)

    age = models.IntegerField()

    gender = models.IntegerField(choices=GENDER_CHOICES,
                                 blank=True, null=True)
