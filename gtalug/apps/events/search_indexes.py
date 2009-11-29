from haystack import indexes
from haystack import site

from gtalug.apps.events.models import Event

class EventIndex(indexes.SearchIndex):
	text = indexes.CharField(document=True, use_template=True)
	date = indexes.DateField(model_attr='date')
	user = indexes.CharField(model_attr='author')
	title = indexes.CharField(model_attr='title')
	content = indexes.CharField(model_attr='tease')
	
	def get_queryset(self):
		return Event.objects.published()

site.register(Event, EventIndex)