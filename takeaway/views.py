from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
import string
import random
from django.template.loader import render_to_string
from LisgreyWebApp_FYP import settings
from food_menus.models import FoodItem
from .models import Basket, BasketItem, TakeawayOrder
from LisgreyWebApp.models import UserProfile
from .forms import TakeawayStatusForm, TakeawayOrderUserForm


def basket_view(request):
    try:
        session_id = request.session['basket_id']
        basket = Basket.objects.get(id=session_id)
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

    return render(request, 'takeaway/basket.html', data)


def nu_confirm_order_user_details_view(request):
    try:
        session_id = request.session['basket_id']
        basket = Basket.objects.get(id=session_id)
    except KeyError:
        session_id = None

        return HttpResponseRedirect('/takeaway/checkout')

    if request.method == 'POST' or None:
        uf = TakeawayOrderUserForm(request.POST or None)

        if uf.is_valid():
            u = uf.save(commit=False)
            order_id_gen = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
            u.order_id = str(order_id_gen)
            u.basket_id = basket.id
            u.save()

            if u.status == "Started":
                del request.session['basket_id']
                del request.session['item_quantities']

            return render(request, 'takeaway/confirm_order.html', {'u': u})

        else:
            return render(request, 'takeaway/takeaway_order_user_details.html', {'form': uf})

    else:
        user_form = TakeawayOrderUserForm()
        return render(request, 'takeaway/takeaway_order_user_details.html', {'form': user_form})


def confirm_order_user_details_view(request):
    try:
        session_id = request.session['basket_id']
        basket = Basket.objects.get(id=session_id)
    except KeyError:
        session_id = None
        return HttpResponseRedirect('/takeaway/checkout')

    uf = TakeawayOrderUserForm(request.POST or None)
    current_user = UserProfile.objects.get(id=request.user.id)
    u = uf.save(commit=False)
    order_id_gen = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    u.order_id = str(order_id_gen)
    u.basket_id = basket.id
    u.first_name = current_user.first_name
    u.last_name = current_user.last_name
    u.contact_phone = current_user.contact_phone
    u.email = current_user.email
    u.save()

    email_template = render_to_string('takeaway/takeaway_confirmation_email.html', {'order_id': u.order_id})
    send_mail(
        'Order Confirmation - ' + u.order_id,
        email_template,
        settings.EMAIL_HOST_USER,
        [current_user.email],
        fail_silently=False,
        )

    if u.status == "Started":
        del request.session['basket_id']
        del request.session['item_quantities']

        return render(request, 'takeaway/confirm_order.html', {'u': u})

    return HttpResponseRedirect('/takeaway/basket')


def update_basket_view(request, food_id):
    try:
        quantity = request.GET.get('quantity')
        u_quantity = True
    except ValueError:
        quantity = None
        u_quantity = False

    try:
        session_id = request.session['basket_id']
        request.session.modified = True

    except KeyError:
        basket_new = Basket()
        basket_new.save()
        request.session['basket_id'] = basket_new.id
        request.session.modified = True
        session_id = basket_new.id

    basket = Basket.objects.get(id=session_id)
    item = FoodItem.objects.get(id=food_id)

    basket_item, created = BasketItem.objects.get_or_create(basket=basket, menu_item=item)

    if created:
        print("yuppa")

    if u_quantity and quantity:
        if int(quantity) == 0:
            basket_item.delete()
        elif int(quantity) < 0:
            basket_item.quantity = 1
        else:
            basket_item.quantity = quantity
            request.session.save()
            basket_item.save()
    else:
        pass

    total = 0.00

    for i in basket.basketitem_set.all():
        food_total = float(i.menu_item.price) * i.quantity
        total += food_total

    request.session['item_quantities'] = basket.basketitem_set.count()
    basket.total = total
    request.session.save()
    basket.save()
    request.session.modified = True

    return HttpResponseRedirect("/takeaway_menu/")


def confirm_order_view(request):
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

    return render(request, 'takeaway/confirm_order.html', data)


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

    return render(request, 'staff_templates/takeaway_orders.html', data)
