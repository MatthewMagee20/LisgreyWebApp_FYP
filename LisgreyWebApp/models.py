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

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class FoodItem(models.Model):
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    allergen = models.ManyToManyField(Allergen)
    description = models.CharField(max_length=150)
    food_quantity = models.IntegerField(default=1)

    def get_all_objects(self):
        queryset = self._meta.model.objects.all()
        return queryset

    def __str__(self):
        return f"{self.name}"


class TakeawayItem(models.Model):
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)


class TakeawayOrder(models.Model):
    # FoodItem
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    food_item = models.ManyToManyField(TakeawayItem)
    total_cost = models.FloatField()
    order_date = models.DateField(auto_now_add=True, blank=True)
    order_time = models.TimeField()
    ordered = models.BooleanField(default=False)


class LoginForm(models.Model):
    username = models.CharField("Enter Username", max_length=50)
    password = models.CharField("Enter Password", max_length=50)
