import datetime

from django.contrib.syndication.feeds import Feed

from gtalug.apps.meetings.models import Meeting

class MeetingFeed(Feed):
	title = 'GTALUG Meetings'
	link = '/'
	description = 'GTALUG meeting feeds.'
	title_template = 'feeds/meeting_title.html'
	description_template = 'feeds/meeting_description.html'
	copyright = 'Creative Commons Attribution 2.5 Canada License'
	
	def items(self):
		return Meeting.objects.eight_days()
	
	def item_link(self, item):
		return item.get_absolute_url()
	
	def item_pubdate(self, item):
		return item.date_modified
	
	def item_enclosure_url(self, item):
		return "http://gtalug.org/%s" % item.get_ical_url()
	
	def item_enclosure_mime_type(self):
		return 'text/calendar'