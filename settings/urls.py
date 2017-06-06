from django.conf.urls import url
from django.contrib import admin
from local_apps.frontend import views as frontend

urlpatterns = [
    url(r'^$', frontend.home, name='home'),
    url(r'^contacto/gracias/', frontend.contact_thanks, name='contact_thanks'),
    url(r'^contacto/', frontend.contact, name='contact'),
    url(r'^adminsite/', admin.site.urls),
]
