from django.urls import path
from .views import basket_view, update_basket_view, confirm_order_view, takeaway_order_view, \
    confirm_order_user_details_view


urlpatterns = [
    path('basket/', basket_view, name='basket'),
    path('basket/update/<int:food_id>/', update_basket_view, name='update_basket'),
    path('checkout/', confirm_order_view, name='confirm_order'),
    path('takeaway_orders/staff/', takeaway_order_view, name='takeaway_orders'),
    path('user_details/', confirm_order_user_details_view, name='user_confirm')
]
