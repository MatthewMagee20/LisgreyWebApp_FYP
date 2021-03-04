from django.contrib import admin

# Register your models here.
from .models import TakeawayOrder, BasketItem

admin.site.register(TakeawayOrder)
admin.site.register(BasketItem)
