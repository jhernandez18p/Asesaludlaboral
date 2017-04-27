from django.conf.urls import url
from django.contrib import admin
from local_apps.frontend import views as frontend

urlpatterns = [
    url(r'^$', frontend.home, name='home'),
    url(r'^admin/', admin.site.urls),
]
