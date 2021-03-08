from django.contrib import admin

# Register your models here.
from .models import FoodItem


@admin.register(FoodItem)
class FoodMenuAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "get_allergen_display")
    list_filter = ("category",)
