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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from LisgreyWebApp import views
from LisgreyWebApp_FYP import settings
from django_email_verification import urls as email_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_password/', views.update_password, name='update_password'),
    path('profile/', views.profile_view, name='profile'),
    # path('contact/', TemplateView.as_view(template_name='gallery.html'), name='contact'),
    path('gallery/', views.gallery_view, name='gallery'),
    # path('account/register/', views.register, name='register'),
    path('account/', include('django.contrib.auth.urls')),

    # path('accounts/', include('django.contrib.auth.urls')),
    path('menus/', include('food_menus.urls')),
    path('reservation/', include('reservations.urls')),
    path('takeaway/', include('takeaway.urls')),
    path('email/', include(email_urls)),
    path('contact/', include('contact.urls')),

    # PWA
    path('', include('pwa.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
