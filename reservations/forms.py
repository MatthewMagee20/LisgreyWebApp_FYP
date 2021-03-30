from django.forms import ModelForm, Textarea, DateInput, TimeInput, ValidationError
from reservations.models import Reservation

from datetime import datetime


class NuReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'email', 'contact_phone', 'date', 'time', 'no_of_people',
                  'additional_information']
        labels = {
            'no_of_people': 'No. of People'
        }

        help_texts = {
            'no_of_people': 'Max 10 People. Please call us for larger reservations. (049) 854 7161'
        }

        widgets = {
            'additional_information': Textarea(attrs={'cols': 5, 'rows': 5}),
            'date': DateInput(attrs={'type': 'datepicker', 'class': 'id_date', 'autocomplete': 'off'}),
            'time': TimeInput(attrs={'class': 'timepicker', 'autocomplete': 'off'})
        }

    def clean(self):
        reservation_time = self.cleaned_data['time']
        reservation_date = self.cleaned_data['date']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        num_people = self.cleaned_data['no_of_people']
        comb = datetime.combine(reservation_date, reservation_time)
        diff = comb - datetime.now()
        errors = []
        f_num_check = False
        l_num_check = False

        print(comb)
        print(datetime.now())
        print(diff)
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

        if datetime.date(datetime.now()) > reservation_date:
            errors.append(ValidationError("Reservation Date cannot be in the past"))

        if diff.total_seconds() <= 3600:  # 3600 seconds = 1 hour
            print(comb)
            print(datetime.now())
            errors.append(ValidationError("Reservation time has to take place in over an hour from current time"))

        if num_people > 10:
            errors.append(ValidationError("Max 10 People. Please call us for reservations with more."))

        if errors:
            raise ValidationError(errors)
