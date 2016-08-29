from asesalud.settings.base import *

SECRET_KEY = config('ASESALUD_SECRET_KEY')

DEBUG = config('ASESALUD_DEBUG',default=False, cast=bool)

ALLOWED_HOSTS = ['.asesaludlaboral.com.ve']

DATABASES ={
            'default':{
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': config('ASESALUD_DB_NAME'),
                'USER': config('ASESALUD_DB_USER'),
                'PASSWORD': config('ASESALUD_DB_PASSWORD'),
                'HOST': config('ASESALUD_DB_HOST'),
                'PORT': config('ASESALUD_DB_PORT',cast=int),
                }
            }
