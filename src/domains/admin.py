from django.contrib import admin

# Register your models here.
from .models import Domain

class DomainModelAdmin(admin.ModelAdmin):
	list_display = ["name", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["name"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["name"]
	class Meta:
		model = Domain


admin.site.register(Domain, DomainModelAdmin)