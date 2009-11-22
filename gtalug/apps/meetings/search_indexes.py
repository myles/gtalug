from haystack import indexes
from haystack import site

from gtalug.apps.meetings.models import Meeting

class MeetingIndex(indexes.SearchIndex):
	text = indexes.CharField(document=True, use_template=True)
	date = indexes.DateField(model_attr='date')
	presenter = indexes.CharField(model_attr='presenter')
		
	def get_queryset(self):
		return Meeting.objects.upcoming_not_tba()

site.register(Meeting, MeetingIndex)