from django.db import models
from LisgreyWebApp.models import UserProfile


# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, editable=False)
    first_name = models.CharField(max_length=100, editable=True, null=False)
    last_name = models.CharField(max_length=100, editable=True, null=False)
    email = models.EmailField(null=False)
    contact_phone = models.CharField(max_length=50, null=False)
    date = models.DateField(editable=True, blank=False)
    time = models.TimeField(editable=True)
    people_quantity = models.IntegerField()
    additional_information = models.CharField(null=True, max_length=20)
    id = models.CharField(unique=True, primary_key=True, max_length=10)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} | {self.date} | {self.time}"
