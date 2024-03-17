from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import models as auth_models


# Just add new fields
# class AppUser(auth_models.AbstractUser):
#     age = models.PositiveIntegerField()


# Completely replace User
# class AppUser(AbstractBaseUser, PermissionsMixin):
#   pass
