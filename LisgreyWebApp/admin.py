from django.contrib import admin
from LisgreyWebApp.models import Reservation, FoodItem, Allergen, Category, Basket, BasketItem

# Register your models here.
admin.site.register(Reservation)
admin.site.register(FoodItem)
admin.site.register(Allergen)
admin.site.register(Category)
admin.site.register(Basket)
admin.site.register(BasketItem)

