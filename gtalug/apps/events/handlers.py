from piston.handler import BaseHandler
from piston.utils import rc, throttle

from gtalug.apps.events.models import Event

class EventListHandler(BaseHandler):
	allowed_methods = ('GET',)
	fields = ('title', 'slug', 'id', 'tease', 'body', 'date', 'time', ('author', ('username', 'first_name', 'last_name')))
	exclued = ('id',)
	model = Post
	
	def read(self, request):
		return Event.objects.published()

class EventDetailHandler(BaseHandler):
	allowed_methods = ('GET',)
	fields = ('title', 'slug', 'tease', 'body', 'date', 'time', ('author', ('username', 'first_name', 'last_name')), 'content_size')
	exclued = ('id',)
	model = Post
	
	@classmethod
	def content_size(self, event):
		return len(event.tease + event.body)
	
	def read(self, request, pk, slug):
		return Event.objects.get(pk=pk, slug=slug)
