from _datetime import datetime

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django_email_verification.confirm import send_email

from LisgreyWebApp.forms import UserRegistrationForm, UserUpdateForm, UserProfile, DeleteUserForm
from reservations.models import Reservation


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':  # if the form has been submitted
        form = UserRegistrationForm(request.POST)  # form bound with post data
        if form.is_valid():
            user = form.save()
            user.is_active = False

            send_email(user)
            return render(request, 'account_confirmation.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_details_form = UserUpdateForm(request.POST, instance=request.user)

        if user_details_form.is_valid():
            update = user_details_form.save()
            update.user = request.user
            update.save()

    else:
        user_details_form = UserUpdateForm(instance=request.user)

    return render(request, 'account/update_profile.html', {'user_details_form': user_details_form})


@login_required
def update_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)

        if password_form.is_valid():
            password = password_form.save()
            update_session_auth_hash(request, password)
            return redirect('profile')

    else:
        password_form = PasswordChangeForm(request.user)

    return render(request, 'account/change_password.html', {'password_form': password_form})


@login_required
def profile_view(request):
    current_user = UserProfile.objects.get(id=request.user.id)
    reservations = Reservation.objects.filter(user=current_user)

    # check if date has passed
    check = datetime.now()

    print(check)
    print(current_user)

    data = {
        'reservations': reservations,
        'date_check': check
    }

    return render(request, 'account/profile.html', data)


def delete_user_view(request):
    if request.method == 'POST':
        DeleteUserForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.info(request, 'Your account has been deleted.')

        return redirect('home')
    else:
        delete_form = DeleteUserForm(instance=request.user)

    context = {
        'delete_form': delete_form
    }

    return render(request, 'account/delete.html', context)

