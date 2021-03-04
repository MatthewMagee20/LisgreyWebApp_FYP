from django.db import models


CATEGORIES = (
    ("Starter", "Starter"),
    ("Main Course", "Main Course"),
    ("Kiddie Menu", "Kiddie Menu"),
    ("Side Order", "Side Order"),
    ("Dessert", "Dessert"),
    ("Drinks", "Drinks"),
)


# Create your models here.
class Allergen(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class FoodItem(models.Model):
    category = models.CharField(max_length=120, choices=CATEGORIES, default="Started")
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    allergen = models.ManyToManyField(Allergen)
    description = models.CharField(max_length=150)

    def get_all_objects(self):
        queryset = self._meta.model.objects.all()
        return queryset

    def __str__(self):
        return f"{self.name}"
