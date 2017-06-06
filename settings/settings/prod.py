from settings.settings.base import *
from decouple import config


ALLOWED_HOSTS = ['asesaludlaboral.com.ve','www.asesaludlaboral.com.ve']

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