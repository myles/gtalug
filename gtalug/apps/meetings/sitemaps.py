from django.contrib.sitemaps import Sitemap

from gtalug.apps.meetings.models import Meeting

class MeetingSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.5
	
	def items(self):
		return Meeting.objects.all_not_tba()
	
	def lastmod(self, obj):
		return obj.date_modified