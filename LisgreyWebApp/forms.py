from django.forms import ModelForm, CharField, PasswordInput
from LisgreyWebApp.models import LoginForm, UserProfile
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm


class LoginForms(ModelForm):
    class Meta:
        model = LoginForm
        fields = "__all__"


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name') + UserCreationForm.Meta.fields + ('email', 'contact_phone',)


    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("Passwords don't match")
    #     return password2
    #
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user


class UserUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'email']
