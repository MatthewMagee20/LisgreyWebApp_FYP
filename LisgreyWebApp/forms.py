from django.forms import ModelForm, Textarea, EmailField, DateField
from LisgreyWebApp.models import Reservation, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bootstrap_datepicker_plus import DatePickerInput


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'people_quantity', 'additional_information']

        widgets = {
            'additional_information': Textarea(attrs={'cols': 5, 'rows': 5}),
            'date': DatePickerInput(),
        }


class LoginForms(ModelForm):
    class Meta:
        model = LoginForm
        fields = "__all__"


class UserRegistrationForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
