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


class UserUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'email']


class DeleteUserForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = []
