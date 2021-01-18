from django.db import models
from django import forms


class Table(models.Model):
    name = models.CharField(max_length=4)


class Reservation(models.Model):
    # table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=20)
    date = models.DateField()
    time = models.TimeField()
    people_quantity = models.IntegerField()
    additional_information = models.CharField(max_length=20)


class Allergen(models.Model):
    name = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)


class FoodItem(models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    allergen = models.ForeignKey(Allergen, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=150)


class TakeawayOrder(models.Model):
    # FoodItem
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, null=True)
    food_quantity = models.IntegerField()
    total_cost = models.FloatField()
    order_time = models.TimeField()
