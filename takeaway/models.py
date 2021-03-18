from django.db import models


# Create your models here.
from food_menus.models import FoodItem


ORDER_TYPE = (
    ("Takeaway", "Takeaway"),
    ("QR", "QR"),
)


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
    full_name = models.CharField(max_length=120)
    contact_phone = models.CharField(max_length=50, null=False)
    order_id = models.CharField(max_length=120, unique=True, default='ABC')
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=120, choices=CHOICES, default="Started")

    def __str__(self):
        return f"{self.order_id}"
