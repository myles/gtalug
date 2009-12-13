from django.conf.urls.defaults import *

urlpatterns = patterns('gtalug.apps.events.views',
	url(r'^$',
		view='list', name='meetings_index'),
	url(r'^(?P<year>\d{4})-(?P<month>\d{2})/$',
		view='list', name='events_list_year_month'),
	
	url(r'^(?P<year>\d{4})-(?P<month>\d{2})/(?P<slug>[-\w]+)/$',
		view='detail', name='events_detail'),
)