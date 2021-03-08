from django.forms import ModelForm
from .models import TakeawayOrder


class TakeawayStatusForm(ModelForm):
    class Meta:
        model = TakeawayOrder
        fields = ['order_id', 'status']
