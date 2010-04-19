from django.contrib import admin

from gtalug.apps.profiles.models import Profile

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'birthday',)

admin.site.register(Profile, ProfileAdmin)