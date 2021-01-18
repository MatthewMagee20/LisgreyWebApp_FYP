from django.shortcuts import render
from LisgreyWebApp.forms import ReservationForm  # TestForm
from django.http import HttpResponseRedirect


def create_reservation_view(request):

    if request.method == 'POST' or None:
        form = ReservationForm(request.POST or None)

        if form.is_valid():
            form.save()
            return render(request, 'reservations/create_reservation.html', {'form': form})

        else:
            form = ReservationForm()
            return render(request, 'reservations/create_reservation.html', {'form': form})

    else:
        form = ReservationForm()
        return render(request, 'reservations/create_reservation.html', {'form': form})

# def add(request):
#     if request.method == "POST" or None:
#         form = TestForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             return render(request, 'reservations/create_reservation.html', {'form': form})
#         else:
#             form = TestForm()
#             return render(request, 'reservations/create_reservation.html', {'form': form})
#     else:
#         form = TestForm()
#         return render(request, 'reservations/create_reservation.html', {'form': form})
