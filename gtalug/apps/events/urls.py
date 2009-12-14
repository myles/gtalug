from django.conf.urls.defaults import *

urlpatterns = patterns('gtalug.apps.events.views',
	url(r'^$',
		view='list', name='events_index'),
	url(r'^(?P<year>\d{4})-(?P<month>\d{2})/$',
		view='list', name='events_list'),
	
	url(r'^(?P<year>\d{4})-(?P<month>\d{2})/(?P<pk>\d+)/$',
		view='detail', name='events_detail_without_slug'),
	url(r'^(?P<year>\d{4})-(?P<month>\d{2})/(?P<pk>\d+)-(?P<slug>[-\w]+)/$',
		view='detail', name='events_detail'),
)