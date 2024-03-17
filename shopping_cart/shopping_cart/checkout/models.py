from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class BillingAddress(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    street_address = models.CharField(
        max_length=100,
    )

    apartment_address = models.CharField(
        max_length=100,
    )

    country = models.CharField(
        max_length=100,
    )

    zip = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.user.username
