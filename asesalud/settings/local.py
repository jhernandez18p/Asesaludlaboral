from asesalud.settings.base import *

STATICFILES_DIRS = ('',)

STATIC_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir),'staticfiles'))

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
