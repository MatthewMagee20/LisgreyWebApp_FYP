from django.contrib import admin

# Register your models here.
from .models import FoodItem, Allergen

admin.site.register(FoodItem)
admin.site.register(Allergen)
