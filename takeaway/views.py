from datetime import datetime
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from LisgreyWebApp_FYP import settings
from food_menus.models import FoodItem
from .models import Basket, BasketItem, TakeawayOrder
from .forms import TakeawayStatusForm, TakeawayOrderUserForm

import config
import random
import string
import urllib
from urllib import parse
import urllib.request
import json


# display basket
def basket_view(request):
    try:
        session_id = request.session['basket_id']

    except KeyError:
        session_id = None

    if session_id:
        basket = Basket.objects.get(id=session_id)

        # if basket is empty
        if basket.basketitem_set.count() == 0:

            data = {
                "basket_is_empty": True
            }

        else:
            data = {
                'basket': basket,
            }

        return render(request, 'takeaway/basket.html', data)

    elif not session_id:
        return HttpResponseRedirect('/menu/')


# user details form for takeaway order
def nu_confirm_order_user_details_view(request):

    # try get session variable for the users basket
    try:
        session_id = request.session['basket_id']
        basket = Basket.objects.get(id=session_id)
    except KeyError:
        return HttpResponseRedirect('/takeaway/checkout')

    if request.method == 'POST' or None:
        uf = TakeawayOrderUserForm(request.POST or None)

        if uf.is_valid():

            # ALL RECAPTCHA COLD IS NOT MY OWN WORK
            # Reference: https://studygyaan.com/django/add-recaptcha-in-your-django-app-increase-security

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': config.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                # ALL CODE AFTER THIS LINE IS MY OWN WORK
                u = uf.save(commit=False)
                order_id_gen = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
                u.order_id = str(order_id_gen)
                u.basket_id = basket.id
                u.save()

                # order confirmation email
                email_template = render_to_string('takeaway/takeaway_confirmation_email.html', {'order_id': u.order_id})
                send_mail(
                    'Order Confirmation - ' + u.order_id,
                    email_template,
                    settings.EMAIL_HOST_USER,
                    [u.email],
                    fail_silently=False,
                    )

                # delete the users session variable if the order has started
                if u.status == "Started":
                    del request.session['basket_id']
                    del request.session['item_quantities']

            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return redirect('nu_user_confirm')

            return render(request, 'takeaway/confirm_order.html', {'u': u})

        else:
            return render(request, 'takeaway/takeaway_order_user_details.html', {'form': uf})

    else:
        user_form = TakeawayOrderUserForm()
        return render(request, 'takeaway/takeaway_order_user_details.html', {'form': user_form})


def update_basket_view(request):

    # try/except clause to try and get quantity of the users input
    # item quantity received through AJAX call in the template
    try:
        quantity = request.GET.get('item_quantity')
        u_quantity = True
    except ValueError:
        quantity = None
        u_quantity = False

    # try/except clause to try and get a basket if it exists.
    # if not, create one
    try:
        session_id = request.session['basket_id']

    except KeyError:
        basket_new = Basket()
        basket_new.save()
        request.session['basket_id'] = basket_new.id
        session_id = basket_new.id

    # get the basket object using the session ID
    # get the food item using the item ID recieved through AJAX
    basket = Basket.objects.get(id=session_id)
    item = FoodItem.objects.get(id=request.GET.get('item_id'))

    basket_item, created = BasketItem.objects.get_or_create(basket=basket, menu_item=item)

    if created:
        quantity = int(quantity) - 1

    if u_quantity and quantity:

        # If item quantity is 0, delete from basket
        if int(quantity) == 0:
            basket_item.delete()

            basket.total = basket.total - (basket_item.menu_item.price * basket_item.quantity)
            if request.session['item_quantities'] <= 0:
                request.session['item_quantities'] = 0

            basket.save()
            return HttpResponseRedirect("/takeaway/basket/")

        # ensure theres not items with quantity less than zero
        elif int(quantity) < 0:
            basket_item.quantity = 1
        else:
            basket_item.quantity = basket_item.quantity + int(quantity)
            print(basket_item.quantity)
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
    return JsonResponse({'item': basket_item.menu_item.name})


# confirmation page displayed to user
def confirm_order_view(request):
    try:
        session_id = request.session['basket_id']
        basket = Basket.objects.get(id=session_id)
    except KeyError:
        return HttpResponse('/takeaway/checkout/')

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

    return render(request, 'takeaway/confirm_order.html', data)


# staff view for managing takeaway orders
def takeaway_order_view(request):
    takeaway_orders = TakeawayOrder.objects.all()
    basket_items = BasketItem.objects.all()
    form = TakeawayStatusForm
    today_date = datetime.date(datetime.now())

    data = {
        'today_date': today_date,
        'takeaway_orders': takeaway_orders,
        'basket_items': basket_items,
        'form': form,
    }

    # allow staff to update the status of order
    if request.method == 'POST' and request.is_ajax():
        status = request.POST.get('order_status')
        order_id = request.POST.get('order_id')

        update_status = TakeawayOrder.objects.get(order_id=order_id)

        update_status.status = status
        update_status.save()
        print(update_status.status)

    return render(request, 'staff_templates/takeaway_orders.html', data)
