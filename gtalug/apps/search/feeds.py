import datetime

from django.utils.feedgenerator import Atom1Feed
from django.contrib.syndication.feeds import Feed

class RssSearchFeed(Feed):
	title = 'GTALUG Search'
	link = 'http://gtalug.org/'
	description = 'GTALUG search feed.'
	copyright = 'Creative Commons Attribution 2.5 Canada License'
	
	author_name = 'Greater Toronto Linux User Group'
	author_link = 'http://gtalug.org/'

class AtomSearchFeed(RssSearchFeed):
	feed_type = Atom1Feed
	subtitle = RssSearchFeed.description