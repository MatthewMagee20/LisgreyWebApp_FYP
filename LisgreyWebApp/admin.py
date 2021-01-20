from django.contrib import admin
from LisgreyWebApp.models import Reservation, FoodItem, Allergen

# Register your models here.
admin.site.register(Reservation)
admin.site.register(FoodItem)
admin.site.register(Allergen)
