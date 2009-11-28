from django.contrib import admin

from gtalug.apps.blog.models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'published', 'date_added', 'date_modified')
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)