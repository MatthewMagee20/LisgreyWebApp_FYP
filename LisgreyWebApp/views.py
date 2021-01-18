from django.shortcuts import render

# Create your views here.

from Lisgrey.forms import ReservationForm


def create_reservation_view(request):
    form = ReservationForm()
    if request.method == 'POST':

        form.save()
        #if form.is_valid():
           # form.save()

    return render(request, 'reservations/create_reservation.html', {'form': form})


