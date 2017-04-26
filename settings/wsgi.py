"""
WSGI config for asesalud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from decouple import config
from django.core.wsgi import get_wsgi_application

if str(config('DEBUG')) == 'True':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings.base")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings.production")

application = get_wsgi_application()
