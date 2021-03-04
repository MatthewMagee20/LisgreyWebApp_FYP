from .forms import ReservationForm
from .models import Reservation
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.


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


def edit_reservation_view(request, reservation_id):
    reservation_instance = Reservation.objects.get(id=reservation_id)
    current_user = request.user

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

    return render(request, 'reservations/edit_reservation.html', {'update_reservation_form': update_reservation_form})
