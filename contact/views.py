from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm

import docker_config
import urllib
from urllib import parse
import urllib.request as rq
import json


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': docker_config.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']

                try:
                    send_mail(subject, message, from_email, [docker_config.EMAIL])
                    messages.success(request, 'Message has been sent!')
                    return redirect('contact')
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            # ''' End reCAPTCHA validation '''
                return redirect('contact')
    return render(request, "contact.html", {'form': form})
