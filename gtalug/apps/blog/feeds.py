import datetime

from django.utils.feedgenerator import Atom1Feed
from django.contrib.syndication.feeds import Feed

from gtalug.apps.blog.models import Post

class RssPostFeed(Feed):
	title = 'GTALUG Blog Posts'
	link = 'http://gtalug.org/blog/'
	description = 'GTALUG blog posts feeds.'
	title_template = 'feeds/blog/title.html'
	description_template = 'feeds/blog/description.html'
	copyright = 'Creative Commons Attribution 2.5 Canada License'
	
	author_name = 'Greater Toronto Linux User Group'
	author_link = 'http://gtalug.org/'
	
	def items(self):
		return Post.objects.published()
	
	def item_link(self, item):
		return item.get_absolute_url()
	
	def item_guid(self, item):
		return item.get_absolute_url()
	
	def item_author_name(self, item):
		return item.author.get_full_name()
	
	def item_pubdate(self, item):
		return item.published

class AtomPostFeed(RssPostFeed):
	feed_type = Atom1Feed
	subtitle = RssPostFeed.description