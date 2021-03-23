from django.urls import path
from .views import get_food_menu_takeaway

urlpatterns = [
    path('menu/', get_food_menu_takeaway, name='takeaway'),
]
