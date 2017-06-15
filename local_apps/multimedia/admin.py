from django.contrib import admin
from local_apps.multimedia.models import (Banner)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
	list_display = ["id","name"]
	list_display_links = ['id']
	list_editable = ["name",]
	list_filter = []
	# search_fields = ["title", "content"]
	
	class Meta:
		model = Banner
