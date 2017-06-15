from django.conf.urls import url
from django.contrib import admin
from local_apps.frontend import views as frontend
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', frontend.home, name='home'),
    url(r'^contacto/gracias/', frontend.contact_thanks, name='contact_thanks'),
    url(r'^contacto/', frontend.contact, name='contact'),
    url(r'^evaluaciones/', frontend.assessment, name='assessment'),
    url(r'^capacitaciones/', frontend.training, name='training'),
    url(r'^asesorias/', frontend.counseling, name='counseling'),
    url(r'^adminsite/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)