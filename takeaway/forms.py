from django.forms import ModelForm
from .models import TakeawayOrder


class TakeawayStatusForm(ModelForm):
    class Meta:
        model = TakeawayOrder
        fields = ['order_id', 'status']


class TakeawayOrderUserForm(ModelForm):
    class Meta:
        model = TakeawayOrder
        fields = ['full_name', 'contact_phone']
