from django.contrib import admin

from gtalug.apps.blog.models import Post

class PostAdmin(admin.ModelAdmin):
	pass

admin.site.register(Post, PostAdmin)