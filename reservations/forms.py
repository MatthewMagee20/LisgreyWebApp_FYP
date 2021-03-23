from django.forms import ModelForm, Textarea, DateInput, TimeInput, ValidationError
from reservations.models import Reservation

from datetime import datetime


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'people_quantity', 'additional_information']

        widgets = {
            'additional_information': Textarea(attrs={'cols': 5, 'rows': 5}),
            'date': DateInput(attrs={'type': 'datepicker', 'class': 'yup', 'autocomplete': 'off'}),
            'time': TimeInput(attrs={'class': 'timepicker', 'autocomplete': 'off'})
        }

    def clean_date(self):
        reservation_date = self.cleaned_data['date']

        if datetime.date(datetime.now()) > reservation_date:
            raise ValidationError("Reservation Date cannot be in the past")
        return reservation_date

    def clean_time(self):
        reservation_time = self.cleaned_data['time']

        if datetime.time(datetime.now()) < reservation_time:
            raise ValidationError("bussion")


class NuReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'email', 'contact_phone', 'date', 'time', 'people_quantity',
                  'additional_information']

        widgets = {
            'additional_information': Textarea(attrs={'cols': 5, 'rows': 5}),
            'date': DateInput(attrs={'type': 'datepicker', 'class': 'yup', 'autocomplete': 'off'}),
            'time': TimeInput(attrs={'class': 'timepicker', 'autocomplete': 'off'})
        }

    def clean(self):
        reservation_time = self.cleaned_data['time']
        reservation_date = self.cleaned_data['date']

        if datetime.date(datetime.now()) > reservation_date:
            raise ValidationError("Reservation Date cannot be in the past")

        comb = datetime.combine(reservation_date, reservation_time)
        print(comb)

        diff = comb - datetime.now()
        print(diff)
        if diff.total_seconds() <= 3600:
            raise ValidationError("Reservation time has to be take place in over an hour")
