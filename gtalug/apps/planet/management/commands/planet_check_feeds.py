import datetime

from django.core.management.base import BaseCommand
from django.db import models

class Command(BaseCommand):
	def handle(self, *args, **options):
		Feed = models.get_model('planet', 'feed')
		feeds = Feed.objects.filter(is_active=True)
		
		import feedparser
		from dateutil.parser import parse as date_parse
		
		for feed in feeds:
			d = feedparser.parse(feed.feed_url)
			
			if not d['status'] == 200:
				feed.is_active = False
				feed.save()
				break
			
			feed.title = d.feed.title
			feed.link = d.feed.link
			feed.tagline = d.feed.subtitle
			try:
				feed.last_modified = date_parse(d.feed.updated)
			except: pass
			feed.last_checked = datetime.datetime.now()
			
			feed.etag = d.etag
			feed.save()