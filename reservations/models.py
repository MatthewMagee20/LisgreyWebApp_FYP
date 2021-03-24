from django.db import models
from LisgreyWebApp.models import UserProfile
from datetime import datetime


# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, editable=False)
    first_name = models.CharField(max_length=100, editable=True, blank=False)
    last_name = models.CharField(max_length=100, editable=True, blank=False)
    email = models.EmailField(blank=False)
    contact_phone = models.CharField(max_length=50, blank=False)
    date = models.DateField(editable=True, null=False, blank=False)
    time = models.TimeField(editable=True, null=False, blank=False)
    no_of_people = models.IntegerField(null=False)
    additional_information = models.CharField(blank=True, max_length=20)
    id = models.CharField(unique=True, primary_key=True, max_length=10)
    confirmed = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(null=False)

    def __str__(self):
        return f"{self.first_name} | {self.date} | {self.time}"

    def reservation_in_past(self):
        reservation_date = self.date
        return datetime.date(datetime.now()) > reservation_date

    def time_over_hour_from_now(self):
        comb = datetime.combine(self.date, self.time)
        diff = comb - datetime.now()
        return diff.total_seconds() >= 3600  # 3600 seconds = 1 hour
