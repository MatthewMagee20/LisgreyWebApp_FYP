from django.forms import ModelForm
from reservations.models import Reservation


class StaffReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
