from django.conf.urls import include, url
from django.contrib import admin

from local_apps.asesorias import views as asesorias_views

urlpatterns = [
    url(r'^$', asesorias_views.asesorias, name="asesorias"),
]
