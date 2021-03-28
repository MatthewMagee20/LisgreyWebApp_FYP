from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from LisgreyWebApp_FYP import settings
from reservations.models import Reservation
from .forms import StaffReservationForm
from django.http import HttpResponseRedirect
from datetime import  datetime


def reservations_view(request):
    reservations = Reservation.objects.all()
    reservation_dates = Reservation.objects.values('date').distinct()
    reservation_times = Reservation.objects.values('time').distinct()
    today_date = datetime.date(datetime.now())

    return render(request, 'staff_templates/staff_reservations.html',
                  {
                      'data': reservations,
                      'dates': reservation_dates,
                      'times': reservation_times,
                      'today_date': today_date,
                  })


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
            print(update.confirmed)

            if update.confirmed == 'Confirmed':
                email_template = render_to_string('reservations/reservation_confirmation_email.html', {'date': date,
                                                                                                       'time': time})
                send_mail(
                    'Reservation Not Available - ' + reservation_id.upper(),
                    email_template,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
            elif update.confirmed == 'Not Available':
                email_template = render_to_string('reservations/reservation_not_available.html', {'date': date,
                                                                                                  'time': time})
                send_mail(
                    'Reservation Confirmation - ' + reservation_id.upper(),
                    email_template,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )

        return HttpResponseRedirect('/admin/staff/reservations/')

    else:
        update_reservation_form = StaffReservationForm(instance=reservation_instance)

    return render(request, 'staff_templates/single_reservation.html',
                  {'update_reservation_form': update_reservation_form})
