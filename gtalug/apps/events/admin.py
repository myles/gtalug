from django.contrib import admin

from gtalug.apps.events.models import Event

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'date', 'date_added', 'date_modified')
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Event, EventAdmin)