from django.contrib import admin
from .models import Reservation


# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", 'contact_phone', "date", "time", "people_quantity", "additional_information")
    list_filter = ("date", )
    search_fields = ("id", "user__username", )