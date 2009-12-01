from django.contrib import admin

from gtalug.apps.planet.models import Feed, Post

class FeedAdmin(admin.ModelAdmin):
	list_display = ('name', 'is_active', 'last_checked',)
	prepopulated_fields = {'slug': ('name',)}
	list_filter = ('is_active', 'last_checked',)
	fieldsets = (
		(None, {
			'fields': ('feed_url', ('name', 'slug'), 'is_active', 'user')
		}),
		('Advanced options', {
			'classes': ('collapse',),
			'fields': (('title', 'link'), 'tagline', 'etag', ('last_modified', 'last_checked'))
		})
	)

class PostAdmin(admin.ModelAdmin):
	list_dispaly = ('title', 'feed',)

admin.site.register(Feed, FeedAdmin)