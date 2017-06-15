from django.contrib import admin
from local_apps.widgets.models import Carousel


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
	list_display = ["id","name","template","position"]
	list_display_links = ['id']
	list_editable = ["template","position"]
	list_filter = ["position"]
	search_fields = ["name"]
	
	class Meta:
		model = Carousel