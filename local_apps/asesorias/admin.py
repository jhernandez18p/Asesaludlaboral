from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Asesorias)
class AsesoriasAdmin(admin.ModelAdmin):

    fields = ('name','title','short_description','description','poster',)
    list_display = ('name','title','short_description','description','poster',)
