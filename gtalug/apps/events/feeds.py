import datetime

from django.utils.feedgenerator import Atom1Feed
from django.contrib.syndication.feeds import Feed

from gtalug.apps.events.models import Event

class RssEventFeed(Feed):
	title = 'GTALUG Events'
	link = 'http://gtalug.org/events/'
	description = 'GTALUG events feed.'
	title_template = 'feeds/events/title.html'
	description_template = 'feeds/events/description.html'
	copyright = 'Creative Commons Attribution 2.5 Canada License'
	
	author_name = 'Greater Toronto Linux User Group'
	author_link = 'http://gtalug.org/'
	
	def items(self):
		return Event.objects.published()
	
	def item_link(self, item):
		return item.get_absolute_url()
	
	def item_guid(self, item):
		return item.get_absolute_url()
	
	def item_author_name(self, item):
		return item.author.get_full_name()
	
	def item_pubdate(self, item):
		return item.date

class AtomPostFeed(RssEventFeed):
	feed_type = Atom1Feed
	subtitle = RssPostFeed.description