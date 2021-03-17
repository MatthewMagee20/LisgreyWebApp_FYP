from django.urls import path
from .views import create_reservation_view, edit_reservation_view, nu_create_reservation_view
from django.views.generic import TemplateView


urlpatterns = [
    path('u/create/', create_reservation_view, name='reservation'),
    path('nu/create/', nu_create_reservation_view, name='nu_reservation'),
    path('edit/<slug:reservation_id>/', edit_reservation_view, name='edit_reservation'),
    path('confirmation/', TemplateView.as_view(template_name='reservations/reservation_confirmation.html')),
]
