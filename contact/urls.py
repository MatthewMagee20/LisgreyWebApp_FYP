from django.urls import path
from django.views.generic import TemplateView

from .views import contactView

urlpatterns = [
    path('contact/', contactView, name='contact'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]