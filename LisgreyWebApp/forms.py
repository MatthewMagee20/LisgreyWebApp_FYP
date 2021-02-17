from django.forms import ModelForm, Textarea, EmailField, DateInput
from LisgreyWebApp.models import Reservation, LoginForm, TakeawayOrder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'people_quantity', 'additional_information']

        widgets = {
            'additional_information': Textarea(attrs={'cols': 5, 'rows': 5}),
            'date': DateInput(attrs={'type': 'date'})
        }


class LoginForms(ModelForm):
    class Meta:
        model = LoginForm
        fields = "__all__"


class UserRegistrationForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

