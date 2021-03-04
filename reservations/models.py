from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    date = models.DateField(editable=True, blank=False)
    time = models.TimeField(editable=True)
    people_quantity = models.IntegerField()
    additional_information = models.CharField(null=True, max_length=20)
