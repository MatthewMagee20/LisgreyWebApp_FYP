from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
from food_menus.models import FoodItem


class Basket(models.Model):
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}"


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, null=True, blank=True)
    menu_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.basket}"


CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)


class TakeawayOrder(models.Model):
    user = models.ForeignKey(get_user_model(), blank=True, on_delete=models.CASCADE, default=1)
    order_id = models.CharField(max_length=120, unique=True, default='ABC')
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=120, choices=CHOICES, default="Started")

    def __str__(self):
        return f"{self.order_id}"
