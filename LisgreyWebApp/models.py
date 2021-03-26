from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    contact_phone = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
