from django.urls import path
from .views import get_food_menu, get_food_menu_takeaway

urlpatterns = [
    path('takeaway_menu/', get_food_menu_takeaway, name='takeaway'),
    path('menu/', get_food_menu, name='menu'),
]
