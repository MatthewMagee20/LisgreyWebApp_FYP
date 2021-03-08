from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
import string
import random

from food_menus.models import FoodItem
from .models import Basket, BasketItem, TakeawayOrder
from .forms import TakeawayStatusForm


def basket_view(request):
    try:
        session_id = request.session['basket_id']
    except KeyError:
        session_id = None
    if session_id:
        basket = Basket.objects.get(id=session_id)

        data = {
            'basket': basket,
        }
    else:
        data = {
            "basket_is_empty": True
        }

    return render(request, 'basket.html', data)


def update_basket_view(request, food_id):
    try:
        quantity = request.GET.get('quantity')
        u_quantity = True
    except ValueError:
        quantity = None
        u_quantity = False

    try:
        session_id = request.session['basket_id']
    except KeyError:
        basket_new = Basket()
        basket_new.save()
        request.session['basket_id'] = basket_new.id
        session_id = basket_new.id
        # print(session_id)

    basket = Basket.objects.get(id=session_id)
    item = FoodItem.objects.get(id=food_id)
    # print("item: " + str(item))

    basket_item, created = BasketItem.objects.get_or_create(basket=basket, menu_item=item)

    if created:
        print("yuppa")

    if u_quantity and quantity:
        if int(quantity) == 0:
            basket_item.delete()
        else:
            basket_item.quantity = quantity
            basket_item.save()
    else:
        pass

    total = 0.00

    for i in basket.basketitem_set.all():
        food_total = float(i.menu_item.price) * i.quantity
        total += food_total

    request.session['item_quantities'] = basket.basketitem_set.count()
    basket.total = total
    basket.save()

    return HttpResponseRedirect("/menus/takeaway_menu/")


def confirm_order_view(request):
    # implement httpredirect
    try:
        session_id = request.session['basket_id']
        basket = Basket.objects.get(id=session_id)
    except KeyError:
        session_id = None

        return HttpResponseRedirect('/takeaway/checkout')

    order, created = TakeawayOrder.objects.get_or_create(basket=basket)

    if created:
        order_id_gen = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        order.order_id = str(order_id_gen)
        order.save()

    if order.status == "Started":

        del request.session['basket_id']
        del request.session['item_quantities']

    data = {
        "order": order
    }

    return render(request, 'confirm_order.html', data)


def takeaway_order_view(request):
    takeaway_orders = TakeawayOrder.objects.all()
    basket_items = BasketItem.objects.all()
    form = TakeawayStatusForm

    data = {
        'takeaway_orders': takeaway_orders,
        'basket_items': basket_items,
        'form': form,
    }

    if request.method == 'POST':
        status = request.POST.get('status')
        yup_id = request.POST.get('order_id')

        update_status = TakeawayOrder.objects.get(order_id=yup_id)

        update_status.status = status
        update_status.save()

    return render(request, 'takeaway_orders.html', data)
