from datetime import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ReservationForm

import config
import random
import string
import urllib
from urllib import parse
import urllib.request
import json


# nu = non user
def nu_create_reservation_view(request):

    # generate a random string 7 letters long
    res_id_gen = ''.join(random.choices(string.digits + string.ascii_lowercase, k=7))

    # if form is submitted
    if request.method == 'POST' or None:
        reservation_form = ReservationForm(request.POST or None)

        # if submitted form contains no errors
        if reservation_form.is_valid():

            # ALL RECAPTCHA CODE IS NOT MY OWN WORK
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

                # save form, dont commit to database
                r = reservation_form.save(commit=False)
                r.id = res_id_gen
                r.time_stamp = datetime.now()
                r.save()
                return HttpResponseRedirect('/reservation/confirmation/')

            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return redirect('nu_reservation')

        else:
            return render(request, 'reservations/create_reservation.html', {'form': reservation_form})

    else:
        reservation_form = ReservationForm()
        return render(request, 'reservations/create_reservation.html', {'form': reservation_form})
