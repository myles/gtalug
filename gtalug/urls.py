from re import escape

from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

from gtalug.apps.meetings.feeds import RssMeetingFeed, AtomMeetingFeed

from gtalug.apps.meetings.sitemaps import MeetingSitemap

admin.autodiscover()

rss_feeds = {
	'meetings': RssMeetingFeed,
}

atom_feeds = {
	'meetings': AtomMeetingFeed,
}

sitemaps = {
	'meetings': MeetingSitemap,
}

urlpatterns = patterns('',
	url(r'^$',
		'django.views.generic.simple.direct_to_template',
		{'template': 'index.html'},
		'homepage',
	),
	
	url(r'^meetings/', include('gtalug.apps.meetings.urls')),
	
	(r'^search/', include('haystack.urls')),
	
	url(r'^rss/(?P<url>.*)/$',
		'django.contrib.syndication.views.feed',
		{ 'feed_dict': rss_feeds },
		name = 'rss_feeds'
	),
	url(r'^atom/(?P<url>.*)/$',
		'django.contrib.syndication.views.feed',
		{ 'feed_dict': atom_feeds },
		name = 'atom_feeds'
	),
	url(r'^sitemap.xml$',
		'django.contrib.sitemaps.views.sitemap',
		{ 'sitemaps': sitemaps }
	),
	
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	
	url(r'^%s/(.*)$' % escape(settings.MEDIA_URL.strip('/')),
		'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
)
