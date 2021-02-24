from django.shortcuts import render, redirect, HttpResponseRedirect
from LisgreyWebApp.forms import ReservationForm, UserRegistrationForm, UserUpdateForm
from LisgreyWebApp.models import FoodItem, Allergen, Basket, BasketItem, TakeawayOrder
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

import string
import random


# create reservation
def create_reservation_view(request):
    if request.method == 'POST' or None:
        reservation_form = ReservationForm(request.POST or None)

        if reservation_form.is_valid():
            reservation_form.save()
            reservation_form.customer = request.user
            return HttpResponseRedirect('/')

        else:
            return render(request, 'reservations/create_reservation.html', {'form': reservation_form})

    else:
        reservation_form = ReservationForm()
        return render(request, 'reservations/create_reservation.html', {'form': reservation_form})


# registration handling
def register(request):
    if request.method == 'POST':  # if the form has been submitted
        form = UserRegistrationForm(request.POST)  # form bound with post data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_details_form = UserUpdateForm(request.POST, instance=request.user)

        if user_details_form.is_valid():
            update = user_details_form.save()
            update.user = request.user
            update.save()

    else:
        user_details_form = UserUpdateForm(instance=request.user)

    return render(request, 'registration/profile.html', {'user_details_form': user_details_form})


def update_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)

        if password_form.is_valid():
            password = password_form.save()
            update_session_auth_hash(request, password)
            return redirect('profile')

    else:
        password_form = PasswordChangeForm(request.user)

    return render(request, 'registration/change_password.html', {'password_form': password_form})


# food menu items
def get_food_menu(request):
    allergens = Allergen.objects.all()
    starter_items = FoodItem.objects.filter(category__name="Starters")
    main_items = FoodItem.objects.filter(category__name="Main")
    dessert_items = FoodItem.objects.filter(category__name="Desserts")
    drink_items = FoodItem.objects.filter(category__name="Drinks")

    data = {
        'allergens': allergens,
        'starters': starter_items,
        'mains': main_items,
        'desserts': dessert_items,
        'drinks': drink_items,
    }

    return render(request, 'menu.html', data)


def get_food_menu_takeaway(request):
    allergens = Allergen.objects.all()
    starter_items = FoodItem.objects.filter(category__name="Starters")
    main_items = FoodItem.objects.filter(category__name="Main")
    dessert_items = FoodItem.objects.filter(category__name="Desserts")
    drink_items = FoodItem.objects.filter(category__name="Drinks")

    data = {
        'allergens': allergens,
        'starters': starter_items,
        'mains': main_items,
        'desserts': dessert_items,
        'drinks': drink_items,
    }

    return render(request, 'takeaway.html', data)


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

    return HttpResponseRedirect("/takeaway/")


def confirm_order_view(request):
    # implement httpredirect
    try:
        session_id = request.session['basket_id']
        basket = Basket.objects.get(id=session_id)
    except KeyError:
        session_id = None
        return HttpResponseRedirect('/takeaway/basket/')

    order, created = TakeawayOrder.objects.get_or_create(basket=basket)

    if created:
        order_id_gen = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        order.order_id = str(order_id_gen)
        order.save()

    if order.status == "Finished":
        del request.session['basket_id']
        del request.session['item_quantities']
    data = {}
    return render(request, 'confirm_order.html', data)


def takeaway_order_view(request):
    takeaway_orders = TakeawayOrder.objects.all()
    basket_items = BasketItem.objects.all()

    data = {
        'takeaway_orders': takeaway_orders,
        'basket_items': basket_items
    }

    return render(request, 'takeaway_orders.html', data)
