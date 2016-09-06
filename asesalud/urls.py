from django.conf.urls import include, url
from django.contrib import admin

from local_apps.frontend import views as front_views

urlpatterns = [
    url(r'^$', front_views.home, name="home"),
    url(r'^asesorias/', include('local_apps.asesorias.urls')),
    url(r'^contact$', front_views.contact, name="contact"),
    url(r'^admin/', admin.site.urls),
]
