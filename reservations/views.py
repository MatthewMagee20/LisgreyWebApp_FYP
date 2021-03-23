from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from LisgreyWebApp.models import UserProfile
from .forms import ReservationForm, NuReservationForm
from .models import Reservation

import random
import string


# create reservation
def create_reservation_view(request):
    res_id_gen = ''.join(random.choices(string.digits + string.ascii_lowercase, k=7))

    if request.user.is_authenticated and request.user.is_active:
        if request.method == 'POST' or None:
            reservation_form = ReservationForm(request.POST or None)
            c_user = UserProfile.objects.get(id=request.user.id)
            if reservation_form.is_valid():
                r = reservation_form.save(commit=False)
                r.first_name = c_user.first_name
                r.last_name = c_user.last_name
                r.email = c_user.email
                r.contact_phone = c_user.contact_phone
                r.time_stamp = datetime.now()
                r.id = res_id_gen
                r.save()
            return HttpResponseRedirect('/reservation/confirmation/')

        else:
            reservation_form = ReservationForm()
            return render(request, 'reservations/create_reservation.html', {'form': reservation_form})

    else:
        reservation_form = ReservationForm()
        return render(request, 'reservations/create_reservation.html', {'form': reservation_form})


def nu_create_reservation_view(request):
    res_id_gen = ''.join(random.choices(string.digits + string.ascii_lowercase, k=7))
    if request.method == 'POST' or None:
        reservation_form = NuReservationForm(request.POST or None)

        if reservation_form.is_valid():
            r = reservation_form.save(commit=False)
            r.id = res_id_gen
            r.time_stamp = datetime.now()
            r.save()
            return HttpResponseRedirect('/reservation/confirmation/')

        else:
            return render(request, 'reservations/create_reservation.html', {'form': reservation_form})

    else:
        reservation_form = NuReservationForm()
        return render(request, 'reservations/create_reservation.html', {'form': reservation_form})


def edit_reservation_view(request, reservation_id):
    reservation_instance = Reservation.objects.get(id=reservation_id)
    current_user = request.user

    if current_user.is_authenticated and current_user.is_active:
        if current_user.id != reservation_instance.user.id:
            print("error")
            return redirect('/')

        if request.method == 'POST':

            update_reservation_form = ReservationForm(request.POST, instance=reservation_instance)

            if update_reservation_form.is_valid():
                update = update_reservation_form.save()
                update.save()

        else:
            update_reservation_form = ReservationForm(instance=reservation_instance)

        return render(request, 'reservations/edit_reservation.html',
                      {'update_reservation_form': update_reservation_form})

    else:
        return render(request, 'account/account_status.html')
