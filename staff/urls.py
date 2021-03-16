from django.urls import path
from django.views.generic import TemplateView
from .views import reservations_view, detail_reservation_view
from takeaway.views import takeaway_order_view

urlpatterns = [
    path('reservations/', reservations_view, name='staff_reservation'),
    path('takeaway_orders/', takeaway_order_view, name='staff_takeaway_orders'),
    path('reservation/<slug:reservation_id>/', detail_reservation_view, name='staff_detail_reservation'),
    path('home/', TemplateView.as_view(template_name='staff templates/staff_home.html'), name='staff_home'),
]
