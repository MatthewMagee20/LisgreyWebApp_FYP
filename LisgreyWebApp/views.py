from django.shortcuts import render, redirect
from LisgreyWebApp.forms import UserRegistrationForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm




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

    return render(request, 'registration/profile.html', {'user_details_form': user_details_form})


def update_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)

        if password_form.is_valid():
            password = password_form.save()
            update_session_auth_hash(request, password)
            return redirect('profile')

    else:
        password_form = PasswordChangeForm(request.user)

    return render(request, 'registration/change_password.html', {'password_form': password_form})



