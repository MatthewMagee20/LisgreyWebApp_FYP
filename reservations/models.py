from django.db import models
from datetime import datetime


class ReservationTable(models.Model):
    table_name = models.CharField(max_length=10)
    table_no_of_people = models.IntegerField()
    available = models.BooleanField(default=True)


class Reservation(models.Model):
    first_name = models.CharField(max_length=100, editable=True, blank=False)
    last_name = models.CharField(max_length=100, editable=True, blank=False)
    email = models.EmailField(blank=False)
    contact_phone = models.CharField(max_length=50, blank=False)
    date = models.DateField(editable=True, null=False, blank=False)
    time = models.TimeField(editable=True, null=False, blank=False)
    no_of_people = models.IntegerField(null=False)
    additional_information = models.TextField(blank=True)
    id = models.CharField(unique=True, primary_key=True, max_length=10)
    confirmed = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(null=False)
    table = models.ForeignKey(ReservationTable, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} | {self.date} | {self.time}"

    def reservation_in_past(self):
        reservation_date = self.date
        return datetime.date(datetime.now()) > reservation_date

    def time_over_hour_from_now(self):
        comb = datetime.combine(self.date, self.time)
        diff = comb - datetime.now()
        return diff.total_seconds() >= 3600  # 3600 seconds = 1 hour
