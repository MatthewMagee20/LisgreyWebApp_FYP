from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from LisgreyWebApp.forms import ReservationForm, UserRegistrationForm
from LisgreyWebApp.models import FoodItem
from django.contrib import messages


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


# food menu items
def get_food_menu(request):
    menu_items = FoodItem.objects.get()
    data = {
        'name': menu_items.name
    }
    return render(request, 'menu.html', data)
