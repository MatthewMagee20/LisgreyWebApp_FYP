"""Application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django_email_verification import urls as email_urls

from LisgreyWebApp import views
from LisgreyWebApp_FYP import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_password/', views.update_password, name='update_password'),
    path('profile/', views.profile_view, name='profile'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('account/register/', views.register, name='register'),
    path('account/', include('django.contrib.auth.urls')),

    path('', include('food_menus.urls')),
    path('reservation/', include('reservations.urls')),
    path('takeaway/', include('takeaway.urls')),
    path('email/', include(email_urls)),
    path('', include('contact.urls')),

    # PWA
    path('', include('pwa.urls')),
    path(r'base_layout', views.base, name='base_layout'),
    path(r'home', views.home, name='home'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
