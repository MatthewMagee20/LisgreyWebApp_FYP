from django.urls import path
from .views import create_reservation_view, edit_reservation_view

urlpatterns = [
    path('', create_reservation_view, name='reservation'),
    path('edit/<int:reservation_id>', edit_reservation_view, name='edit_reservation')
]
