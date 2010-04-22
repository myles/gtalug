from django.contrib import admin

from gtalug.apps.meetings.models import Meeting

class MeetingAdmin(admin.ModelAdmin):
	list_display = ('topic', 'tba', 'date', 'time')
	prepopulated_fields = {'slug': ('topic',)}
	list_filter = ('tba',)
	date_hierarchy = 'date'
	search_field = ('topic', 'tease', 'body')

admin.site.register(Meeting, MeetingAdmin)