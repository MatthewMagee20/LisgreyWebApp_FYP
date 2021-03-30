from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import TakeawayOrder


class TakeawayStatusForm(ModelForm):
    class Meta:
        model = TakeawayOrder
        fields = ['order_id', 'status']


class TakeawayOrderUserForm(ModelForm):
    class Meta:
        model = TakeawayOrder
        fields = ['first_name', 'last_name', 'email', 'contact_phone']

    def clean(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        errors = []
        f_num_check = False
        l_num_check = False

        for char in first_name:
            if char.isdigit():
                f_num_check = True
                break
        if f_num_check:
            errors.append(ValidationError("First name cannot contain a number"))

        for char in last_name:
            if char.isdigit():
                l_num_check = True
                break
        if l_num_check:
            errors.append(ValidationError("Last Name cannot contain a number"))

        if errors:
            raise ValidationError(errors)
