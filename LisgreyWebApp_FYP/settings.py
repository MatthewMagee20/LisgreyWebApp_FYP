from django.contrib import messages
from pathlib import Path
from django.contrib.auth import login

import os
import socket
import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.DEPLOY_SECURE

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
    'corsheaders',
    'pwa',
    'contact',
    'staff',
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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lisgrey_database',
        'USER': 'postgres',
        'PASSWORD': config.PRODUCTION_PASSWORD,
        'HOST': '127.0.0.1',
        'PORT': '25432'
    }
}

# Password validation
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

# Crispy Forms Library
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_FAIL_SILENTLY = not DEBUG

BOOTSTRAP4 = {
    'include_jquery': True,
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'WET'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TIME_INPUT_FORMATS = [
    '%H:%M %p'
]

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# if development on local machine
if socket.gethostname() == "acer":
    DATABASES["default"]["HOST"] = "localhost"
    DATABASES["default"]["PORT"] = 25432
    DATABASES["default"]["PASSWORD"] = 'password'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_PAGE_DOMAIN = 'http://localhost:8000'

# if production
else:
    DATABASES["default"]["HOST"] = "lisgrey-psql"
    DATABASES["default"]["PORT"] = 5432
    DATABASES["default"]["PASSWORD"] = config.PRODUCTION_PASSWORD
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_PAGE_DOMAIN = 'www.lisgreyhouse.com'

# Set DEPLOY_SECURE to True only for LIVE deployment
if config.DEPLOY_SECURE:
    DEBUG = False  # Turn Debug mode off
    TEMPLATES[0]["OPTIONS"]["debug"] = False
    ALLOWED_HOSTS = ['.lisgreyhouse.com', 'localhost', '138.68.130.143', '127.0.0.1', '192.168.1.145']
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

else:
    DEBUG = True
    TEMPLATES[0]["OPTIONS"]["debug"] = True
    ALLOWED_HOSTS = ['*', ]
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False

# Email backend
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config.EMAIL
EMAIL_HOST_PASSWORD = config.PASSWORD
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = config.EMAIL


# PWA Settings
# https://github.com/silviolleite/django-pwa
PWA_APP_NAME = 'Lisgrey House'
PWA_APP_DESCRIPTION = "Lisgrey House Web Appalication"
PWA_APP_THEME_COLOR = '#39606F'
PWA_APP_BACKGROUND_COLOR = '#39606F'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/images/icons/android-chrome-192x192.png',
        'sizes': '192x192'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/images/icons/apple-touch-icon.png',
        'sizes': '152x1524'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/icons/android-chrome-512x512.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')

# Django Messages
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
MESSAGE_TAGS = {
    messages.ERROR: 'alert-danger',
    messages.SUCCESS: 'alert-success'
}
