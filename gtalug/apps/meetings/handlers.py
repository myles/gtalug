from piston.handler import BaseHandler
from piston.utils import rc, throttle

from gtalug.apps.meetings.models import Meeting

class MeetingListHandler(BaseHandler):
	allowed_methods = ('GET',)
	fields = ('topic', 'slug', 'id', 'tease', 'body', 'date', 'time', 'presenter')
	model = Meeting
	
	def read(self, request, year=None):
		if year:
			return Meeting.objects.all_not_tba(date__year=year)
		else:
			return Meeting.objects.all_not_tba()
			

class MeetingDetailHandler(BaseHandler):
	allowed_methods = ('GET',)
	fields = ('topic', 'slug', 'id', 'tease', 'body', 'date', 'time', 'presenter')
	model = Meeting
	
	@classmethod
	def content_size(self, meeting):
		return len(meeting.body)
	
	def read(self, request, year, month, slug=None):
		if slug:
			return Meeting.objects.get(slug__iexact=slug, date__year=year, date__month=month)
		else:
			return Meeting.objects.get(date__year=year, date__month=month)

class MeetingNextHandler(BaseHandler):
	allowed_methods = ('GET',)
	fields = ('topic', 'slug', 'id', 'tease', 'body', 'date', 'time', 'presenter')
	model = Meeting
	
	@classmethod
	def content_size(self, meeting):
		return len(meeting.body)
	
	def read(self, request):
		return Meeting.objects.upcoming()[0]