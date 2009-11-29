from django.contrib.sitemaps import Sitemap

from gtalug.apps.events.models import Event

class EventSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.5
	
	def items(self):
		return Event.objects.published()
	
	def lastmod(self, obj):
		return obj.date_modified