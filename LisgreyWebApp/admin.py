from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Image
from LisgreyWebApp.models import UserProfile
from .forms import UserRegistrationForm


# Register your models here.


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    add_form = UserRegistrationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'contact_phone', 'password1', 'password2')}
         ),
    )


admin.site.register(Image)
admin.site.register(UserProfile, UserAdmin)
