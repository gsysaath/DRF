from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
