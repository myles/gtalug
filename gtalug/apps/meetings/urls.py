from django.conf.urls.defaults import *

urlpatterns = patterns('gtalug.apps.meetings.views',
	url(r'^(?P<year>\d{4})-(?P<month>\d{2})/$',
		view='detail', name='meetings_detail_without_slug'),
	url(r'^(?P<year>\d{4})-(?P<month>\d{2})/(?P<slug>[-\w]+)/$',
		view='detail', name='meetings_detail'),
)