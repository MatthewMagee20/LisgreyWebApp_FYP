from django.db import models
from django.contrib.auth import get_user_model


class Table(models.Model):
    name = models.CharField(max_length=4)


class Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    date = models.DateField(editable=True, blank=False)
    time = models.TimeField(editable=True)
    people_quantity = models.IntegerField()
    additional_information = models.CharField(null=True, max_length=20)


class Allergen(models.Model):
    name = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)


class FoodItem(models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    allergen = models.ManyToManyField(Allergen)
    description = models.CharField(max_length=150)


class TakeawayOrder(models.Model):
    # FoodItem
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, null=True)
    food_quantity = models.IntegerField()
    total_cost = models.FloatField()
    order_time = models.TimeField()


class LoginForm(models.Model):
    username = models.CharField("Enter Username", max_length=50)
    password = models.CharField("Enter Password", max_length=50)
