from django.contrib import admin
from .models import Reservation


# admin.site.unregister(ReservationTable)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("id", 'confirmed', "first_name", 'contact_phone', "date", "time", "no_of_people",
                    "additional_information")
    list_filter = ("date", )
    search_fields = ("id", "user__username", )
