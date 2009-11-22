from django.contrib import admin

from gtalug.apps.meetings.models import Meeting

class MeetingAdmin(admin.ModelAdmin):
	list_display = ('topic', 'date', 'time')
	prepopulated_fields = {'slug': ('topic',)}

admin.site.register(Meeting, MeetingAdmin)