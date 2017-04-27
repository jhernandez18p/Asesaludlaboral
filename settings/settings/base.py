# -*- coding: utf-8 -*-
import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')
ROOT_URLCONF = 'settings.urls'
WSGI_APPLICATION = 'settings.wsgi.application'
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

if DEBUG:
    # print("Hello world %s " % (str(DEBUG)))
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
    ALLOWED_HOSTS = ['192.34.61.100', 'asesaludlaboral.com.ve', 'www.asesaludlaboral.com.ve']
    SITE_URL = 'http://asesaludlaboral.com.ve'
    DATABASES = {
        'default':{
            'ENGINE':config('DB_ENGINE'),
            'NAME':config('DB_NAME'),
            'USER':config('DB_USER'),
            'PASSWORD':config('DB_PASSWORD'),
            'HOST':config('DB_HOST'),
            'PORT':config('DB_PORT', cast=int),
        }
    }
    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
        'local_apps.profiles.EmailBackend.EmailBackend',
    ]

LOGIN_URL = 'dashboard'
LOGIN_REDIRECT_URL = '/dashboard/'
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

