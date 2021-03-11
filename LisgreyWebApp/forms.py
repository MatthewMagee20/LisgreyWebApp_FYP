from django.forms import ModelForm, CharField, ValidationError, PasswordInput
from LisgreyWebApp.models import LoginForm, UserProfile


class LoginForms(ModelForm):
    class Meta:
        model = LoginForm
        fields = "__all__"


class UserRegistrationForm(ModelForm):
    password1 = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Password confirmation', widget=PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'email', 'contact_phone', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'email']
