from haystack import indexes
from haystack import site

from django.contrib.sites.models import Site
from django.contrib.flatpages.models import FlatPage

class FlatPageIndex(indexes.SearchIndex):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')
	
	def get_queryset(self):
		_site = Site.objects.get_current()
		return FlatPage.objects.filter(sites__in=[_site], registration_required=False)

site.register(FlatPage, FlatPageIndex)