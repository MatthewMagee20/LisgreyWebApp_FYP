from django.db import models
from datetime import datetime


class Reservation(models.Model):

    RESERVATION_STATUS = (
        ("Confirmed", "Confirmed"),
        ("Awaiting Confirmation", "Awaiting Confirmation"),
        ("Not Available", "Not Available"),
    )

    first_name = models.CharField(max_length=100, editable=True, blank=False)
    last_name = models.CharField(max_length=100, editable=True, blank=False)
    email = models.EmailField(blank=False)
    contact_phone = models.CharField(max_length=12, blank=False)
    date = models.DateField(editable=True, null=False, blank=False)
    time = models.TimeField(editable=True, null=False, blank=False)
    no_of_people = models.IntegerField(null=False)
    additional_information = models.TextField(blank=True)
    id = models.CharField(unique=True, primary_key=True, max_length=10)
    confirmed = models.CharField(choices=RESERVATION_STATUS, max_length=25, default="Awaiting Confirmation")
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
