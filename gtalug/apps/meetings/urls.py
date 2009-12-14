from django.conf.urls.defaults import *

urlpatterns = patterns('gtalug.apps.meetings.views',
	url(r'^$',
		view='list', name='meetings_index'),
	url(r'^(?P<year>\d{4})/$',
		view='list', name='meetings_list'),
	
	url(r'^(?P<year>\d{4})-(?P<month>\d{2})/$',
		view='detail', name='meetings_detail_without_slug'),
	url(r'^(?P<year>\d{4})-(?P<month>\d{2})/(?P<slug>[-\w]+)/$',
		view='detail', name='meetings_detail'),
	
	url(r'^next/$',
		view='next', name='next_meeting'
	)
)