from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$',
		view='gtalug.apps.search.views.search', name='haystack_search'),
	url(r'^opensearch\.xml$',
		'django.views.generic.simple.direct_to_template',
		{'template': 'search/opensearch.xml', 'mimetype': 'text/xml'},
		'opensearch')
)