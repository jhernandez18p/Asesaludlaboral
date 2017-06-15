from django.contrib import admin
from local_apps.frontend.models import (Site, Template)
# Register your models here.

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
	list_display = ["id","name"]
	list_display_links = ['id']
	list_editable = ["name",]
	list_filter = []
	# search_fields = ["title", "content"]
	
	class Meta:
		model = Site


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
	list_display = ["id","name","template"]
	list_display_links = ['id']
	list_editable = ["template",]
	list_filter = []
	# search_fields = ["title", "content"]
	
	class Meta:
		model = Template