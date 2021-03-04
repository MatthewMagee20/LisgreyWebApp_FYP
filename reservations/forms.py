from django.forms import ModelForm, Textarea, DateInput

from reservations.models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'people_quantity', 'additional_information']

        widgets = {
            'additional_information': Textarea(attrs={'cols': 5, 'rows': 5}),
            'date': DateInput(attrs={'type': 'date'})
        }
