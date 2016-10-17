from django.conf.urls import include, url
from django.contrib import admin

from local_apps.blog import views as blog_views

urlpatterns = [
    url(r'^$', blog_views.blog, name="blog"),
]
