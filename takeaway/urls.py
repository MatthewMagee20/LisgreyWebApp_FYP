from django.urls import path
from .views import basket_view, update_basket_view, confirm_order_view, nu_confirm_order_user_details_view

urlpatterns = [
    path('basket/', basket_view, name='basket'),
    path('basket/update/', update_basket_view, name='update_basket'),
    path('checkout/', confirm_order_view, name='confirm_order'),
    path('contact_information/', nu_confirm_order_user_details_view, name='nu_user_confirm'),
]
