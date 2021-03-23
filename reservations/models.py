from django.db import models
from LisgreyWebApp.models import UserProfile


# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, editable=False)
    first_name = models.CharField(max_length=100, editable=True, blank=False)
    last_name = models.CharField(max_length=100, editable=True, blank=False)
    email = models.EmailField(blank=False)
    contact_phone = models.CharField(max_length=50, blank=False)
    date = models.DateField(editable=True, null=True)
    time = models.TimeField(editable=True, null=True)
    no_of_people = models.IntegerField(null=False)
    additional_information = models.CharField(blank=True, max_length=20)
    id = models.CharField(unique=True, primary_key=True, max_length=10)
    status = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(null=False)

    def __str__(self):
        return f"{self.first_name} | {self.date} | {self.time}"
