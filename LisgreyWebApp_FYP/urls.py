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
from LisgreyWebApp import views
from LisgreyWebApp_FYP import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('privacy/', TemplateView.as_view(template_name='privacy_policy.html'), name='privacy'),
    path('cookies/', TemplateView.as_view(template_name='cookie_policy.html'), name='cookies'),
    path('gallery/', TemplateView.as_view(template_name="gallery.html"), name='gallery'),
    path('', include('food_menus.urls')),
    path('reservation/', include('reservations.urls')),
    path('takeaway/', include('takeaway.urls')),
    path('', include('contact.urls')),
    path('admin/staff/', include('staff.urls')),

    # PWA
    path('', include('pwa.urls')),
    path(r'offline', views.offline, name='offline'),
    path(r'404', views.error, name='error'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
