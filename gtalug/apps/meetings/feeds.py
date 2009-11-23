import datetime

from django.utils.feedgenerator import Atom1Feed
from django.contrib.syndication.feeds import Feed

from gtalug.apps.meetings.models import Meeting

class RssMeetingFeed(Feed):
	title = 'GTALUG Meetings'
	link = 'http://gtalug.org/'
	description = 'GTALUG meeting feeds.'
	title_template = 'feeds/meetings/title.html'
	description_template = 'feeds/meetings/description.html'
	copyright = 'Creative Commons Attribution 2.5 Canada License'
	
	author_name = 'Greater Toronto Linux User Group'
	author_link = 'http://gtalug.org/'
	
	def items(self):
		return Meeting.objects.eight_days()
	
	def item_link(self, item):
		return item.get_absolute_url()
	
	def item_guid(self, item):
		return item.get_absolute_url()
	
	def item_author_name(self, item):
		if item.presenter_user:
			return item.presenter_user.get_full_name()
		else:
			return item.presenter
	
	def item_pubdate(self, item):
		return item.date_modified

class AtomMeetingFeed(RssMeetingFeed):
	feed_type = Atom1Feed
	subtitle = RssMeetingFeed.description