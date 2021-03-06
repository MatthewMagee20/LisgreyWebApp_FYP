"""
Django settings for LisgreyWebApp_FYP project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import socket
from pathlib import Path

from whitenoise.storage import CompressedManifestStaticFilesStorage

import docker_config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = docker_config.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'LisgreyWebApp',
    'reservations',
    'takeaway',
    'food_menus',
    'crispy_forms',
    'bootstrap4',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'LisgreyWebApp_FYP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LisgreyWebApp_FYP.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lisgrey_database',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '25432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_FAIL_SILENTLY = not DEBUG

BOOTSTRAP4 = {
    'include_jquery': True,
}

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'  # new

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# Add this line to access static files on templates
STATIC_URL = "/static/"
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'dist')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

TIME_INPUT_FORMATS = [
    '%H:%M %p'
]

DATE_INPUT_FORMATS = [
    '%d-%m-%Y'
]

if socket.gethostname() == "acer":
    DATABASES["default"]["HOST"] = "localhost"
    DATABASES["default"]["PORT"] = '25432'
else:
    DATABASES["default"]["HOST"] = "lisgrey_database"
    DATABASES["default"]["PORT"] = '5432'

# Set DEPLOY_SECURE to True only for LIVE deployment
if docker_config.DEPLOY_SECURE:
    DEBUG = False
    TEMPLATES[0]["OPTIONS"]["debug"] = False
    ALLOWED_HOSTS = ['.matthewmawm.xyz', 'localhost', '142.93.47.106', '127.0.0.1']
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    CORS_ORIGIN_ALLOW_ALL = True
else:
    DEBUG = True
    TEMPLATES[0]["OPTIONS"]["debug"] = True
    ALLOWED_HOSTS = ['*', ]
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False