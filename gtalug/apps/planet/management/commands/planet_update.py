import datetime

from django.core.management.base import BaseCommand
from django.db import models

class Command(BaseCommand):
	def handle(self, *args, **options):
		Feed = models.get_model('planet', 'feed')
		Post = models.get_model('planet', 'post')
		
		import feedparser
		from dateutil.parser import parse as date_parse
		
		feeds = Feed.objects.filter(is_active=True)
		
		for feed in feeds:
			d = feedparser.parse(feed.feed_url)
			
			if not d['status'] == 200:
				feed.is_active = False
				feed.save()
				break
			
			for entry in d.entries:
				post, created = Post.objects.get_or_create(guid=entry.guid,
					defaults={ 'feed': feed })
				if created:
					post.title = entry.title
					post.link = entry.link
					post.content = entry.description
					post.guid = entry.guid
					
					if entry.get('author_detail', None):
						post.author = entry.author_detail.name
						post.author_email = entry.author_detail.email
					
					post.date_modified = date_parse(entry.updated)
					
					post.save()