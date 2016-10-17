from django.conf.urls import include, url
from django.contrib import admin

from local_apps.capacitaciones import views as capacitaciones_views

urlpatterns = [
    url(r'^$', capacitaciones_views.capacitaciones, name="capacitaciones"),
]
