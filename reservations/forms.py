from django.forms import ModelForm, Textarea, DateInput, TimeInput

from reservations.models import Reservation


class ReservationForm(ModelForm):

    class Meta:
        model = Reservation
        fields = ['date', 'time', 'people_quantity', 'additional_information']

        widgets = {
            'additional_information': Textarea(attrs={'cols': 5, 'rows': 5}),
            'date': DateInput(attrs={'type': 'datepicker', 'class': 'yup', 'autocomplete': 'off'}),
            'time': TimeInput(attrs={'class': 'timepicker', 'autocomplete': 'off'})
        }
