from django.forms import ModelForm, Textarea, TimeInput
from Lisgrey.models import Reservation
from bootstrap_datepicker_plus import DatePickerInput


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'date', 'time', 'people_quantity', 'additional_information']

        widgets = {
            'additional_information': Textarea(attrs={'cols': 5, 'rows': 5}),
            'date': DatePickerInput(format='%d/%m/%Y'),
            'time': TimeInput(format='%H:%M')
        }
