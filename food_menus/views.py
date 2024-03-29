from django.shortcuts import render
from .models import FoodItem


def get_food_menu_takeaway(request):

    starter_items = FoodItem.objects.filter(category="Starter")
    main_items = FoodItem.objects.filter(category="Main Course")
    kids_menu_items = FoodItem.objects.filter(category="Kiddie Menu")
    side_orders = FoodItem.objects.filter(category="Side Order")
    dessert_items = FoodItem.objects.filter(category="Dessert")
    drink_items = FoodItem.objects.filter(category="Drinks")

    data = {
        'starters': starter_items,
        'mains': main_items,
        'kids_items': kids_menu_items,
        'side_orders': side_orders,
        'desserts': dessert_items,
        'drinks': drink_items,
        'allergens': FoodItem.ALLERGENS
    }

    return render(request, 'food_menus/menu.html', data)
