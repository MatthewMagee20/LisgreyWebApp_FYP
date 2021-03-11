from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    contact_phone = models.CharField(max_length=100)


class LoginForm(models.Model):
    username = models.CharField("Enter Username", max_length=50)
    password = models.CharField("Enter Password", max_length=50)


class Image(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='static/images/')

    def __unicode__(self):
        return self.title
