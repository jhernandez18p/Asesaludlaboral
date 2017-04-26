from settings.settings.base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG',default=False, cast=bool)

ALLOWED_HOSTS = ['asesaludlaboral.com.ve','www.asesaludlaboral.com.ve']

DATABASES ={
            'default':{
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': config('DB_NAME'),
                'USER': config('DB_USER'),
                'PASSWORD': config('DB_PASSWORD'),
                'HOST': config('DB_HOST'),
                'PORT': config('DB_PORT',cast=int),
                }
            }
