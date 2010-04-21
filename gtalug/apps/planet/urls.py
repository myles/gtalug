from django.conf.urls.defaults import *

urlpatterns = patterns('gtalug.apps.planet.views',
	url(r'^$',
		view='index', name='planet_index'),
	
	url(r'^(?P<slug>[-\w]+)/$',
		view='feed_detail', name='planet_feed_detail'),
	
	url(r'^(?P<slug>[-\w]+)/(?P<pk>\d+)/$',
		view='post_detail', name='planet_post_detail'),
)