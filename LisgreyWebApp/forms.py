from django.core.exceptions import ValidationError
from django.forms import ModelForm
from LisgreyWebApp.models import LoginForm, UserProfile
from django.contrib.auth.forms import UserCreationForm


class LoginForms(ModelForm):
    class Meta:
        model = LoginForm
        fields = "__all__"


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name') + UserCreationForm.Meta.fields + ('email', 'contact_phone',)

    def clean(self):
        f_num_check = False
        l_num_check = False
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        errors = []

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


class UserUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'email']


class DeleteUserForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = []
