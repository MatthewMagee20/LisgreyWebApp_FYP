from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
from django.template.loader import render_to_string

from LisgreyWebApp_FYP import settings
from reservations.models import Reservation
from .forms import StaffReservationForm
from django.http import HttpResponseRedirect

from LisgreyWebApp.forms import LoginForms


def reservations_view(request):
    reservations = Reservation.objects.all()
    reservation_dates = Reservation.objects.values('date').distinct()
    print(reservation_dates.dates)

    return render(request, 'staff_templates/staff_reservations.html',
                  {'data': reservations, 'dates': reservation_dates}
                  )


def detail_reservation_view(request, reservation_id):
    reservation_instance = Reservation.objects.get(id=reservation_id)

    if request.method == 'POST':

        update_reservation_form = StaffReservationForm(request.POST, instance=reservation_instance)

        if update_reservation_form.is_valid():
            update = update_reservation_form.save(commit=False)
            email = update.email
            date = update.date
            time = update.time
            update.save()

            if update.status:
                email_template = render_to_string('reservations/reservation_confirmation_email.html', {'date': date,
                                                                                                       'time': time})
                send_mail(
                    'Reservation Confirmation - ' + reservation_id,
                    email_template,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                    )

        return HttpResponseRedirect('/staff/reservations')

    else:
        update_reservation_form = StaffReservationForm(instance=reservation_instance)

    return render(request, 'staff_templates/single_reservation.html',
                  {'update_reservation_form': update_reservation_form})
