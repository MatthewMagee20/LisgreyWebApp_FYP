from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Reservation(models.Model):
    full_name = models.CharField(max_length=100, editable=True)
    contact_phone = models.CharField(max_length=50, null=False)
    date = models.DateField(editable=True, blank=False)
    time = models.TimeField(editable=True)
    people_quantity = models.IntegerField()
    additional_information = models.CharField(null=True, max_length=20)
    id = models.CharField(unique=True, primary_key=True, max_length=10)

    def __str__(self):
        return f"{self.full_name} | {self.date} | {self.time}"
