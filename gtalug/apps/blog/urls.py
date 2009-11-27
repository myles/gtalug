from django.conf.urls.defaults import *

urlpatterns = patterns('gtalug.apps.blog.views',
	url(r'^$',
		view='index', name='blog_index'),
	
	url(r'^(?P<pk>\d+)/$',
		view='detail', name='blog_post_detail_without_slug'),
	url(r'^(?P<pk>\d+)-(?P<slug>[-\w]+)/$',
		view='detail', name='blog_post_detail'),
)