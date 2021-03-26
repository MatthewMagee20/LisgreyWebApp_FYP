from django.urls import path
from .views import nu_create_reservation_view
from django.views.generic import TemplateView


urlpatterns = [
    path('nu/create/', nu_create_reservation_view, name='nu_reservation'),
    path('confirmation/', TemplateView.as_view(template_name='reservations/reservation_confirmation.html')),
]
