from django.forms import ModelForm, Textarea
from LisgreyWebApp.models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

        widgets = {
            'additional_information': Textarea(attrs={'cols': 5, 'rows': 5}),
        }


#class TestForm(ModelForm):
#    text = CharField(error_messages={'required': 'Please enter your name'})
#
#    class Meta:
#        model = Test
#        fields = ('text',)
