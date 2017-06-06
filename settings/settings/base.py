# -*- coding: utf-8 -*-
import os
from decouple import config

DEBUG = config('DEBUG')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('SECRET_KEY')
ROOT_URLCONF = 'settings.urls'

if DEBUG:
    # print("Hello world %s " % (str(DEBUG)))
    WSGI_APPLICATION = 'settings.wsgi.application'
    ALLOWED_HOSTS = ['*']
    SITE_URL = '/'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

else:
    # print("Hello cruel world %s " % (str(DEBUG)))
    WSGI_APPLICATION = 'settings.wsgi_prod.application'

LANGUAGE_CODE = 'es-VE'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR, os.pardir), 'media'))
STATICFILES_DIRS = (
    os.path.abspath(os.path.join(os.path.join(BASE_DIR, os.pardir), 'staticfiles')),
)
# STATIC_ROOT = os.path.abspath(
#     os.path.join(os.path.join(BASE_DIR,os.pardir),'staticfiles'))
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.abspath(os.path.join(os.path.join(BASE_DIR, os.pardir), 'templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'settings.settings.custom_context_processors.menu',
                'settings.settings.custom_context_processors.sessions',
            ],
        },
    },
]
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
LOCAL_APPS = []
THIRDPARTY_APPS = []
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRDPARTY_APPS
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'local_apps.profiles.EmailBackend.EmailBackend',
]

LOGIN_URL = 'dashboard'
LOGIN_REDIRECT_URL = '/dashboard/'
SITE_URL = 'http://wwww.asesaludlaboral.com.ve'
LOGOUT_REDIRECT_URL = SITE_URL
SESSION_COOKIE_AGE = 43200
SESSION_COOKIE_NAME = 'session'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
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

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'obediencia1212'
EMAIL_HOST_USER = 'asesaludlaboral2727ca@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER