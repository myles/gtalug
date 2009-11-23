from django.contrib.sitemaps import Sitemap

from gtalug.apps.blog.models import Post

class PostSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.5
	
	def items(self):
		return Post.objects.published()
	
	def lastmod(self, obj):
		return obj.date_modified