from django.db import models


class LoginForm(models.Model):
    username = models.CharField("Enter Username", max_length=50)
    password = models.CharField("Enter Password", max_length=50)


class Image(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='static/images/')

    def __unicode__(self):
        return self.title
