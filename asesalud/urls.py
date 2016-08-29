from django.conf.urls import url
from django.contrib import admin

from local_apps.frontend import views as front_views
urlpatterns = [
    # url(r'^$', front_views.home, name="home"),
    url(r'^admin/', admin.site.urls),
]
