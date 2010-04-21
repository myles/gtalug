from haystack import indexes
from haystack import site

from gtalug.apps.profiles.models import Profile

class ProfileIndex(indexes.SearchIndex):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='get_name')
	content = indexes.CharField(model_attr='bio')
	user = indexes.CharField(model_attr='user')
	
	def get_queryset(self):
		return Profile.objects.all()

site.register(Profile, ProfileIndex)