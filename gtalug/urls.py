from re import escape

from django.contrib import admin
from django.conf import settings
from django.conf.urls.defaults import *

from gtalug.apps.meetings.feeds import RssMeetingFeed, AtomMeetingFeed
from gtalug.apps.blog.feeds import RssPostFeed, AtomPostFeed

from gtalug.apps.meetings.sitemaps import MeetingSitemap
from gtalug.apps.blog.sitemaps import PostSitemap

admin.autodiscover()

rss_feeds = {
	'meetings': RssMeetingFeed,
	'blog': RssPostFeed,
}

atom_feeds = {
	'meetings': AtomMeetingFeed,
	'blog': AtomPostFeed,
}

sitemaps = {
	'meetings': MeetingSitemap,
	'posts': PostSitemap,
}

urlpatterns = patterns('',
	url(r'^$',
		'django.views.generic.simple.direct_to_template',
		{'template': 'home/index.html'},
		'homepage',
	),
	
	url(r'^meetings/', include('gtalug.apps.meetings.urls')),
	url(r'^blog/', include('gtalug.apps.blog.urls')),
	
	url(r'^search/', include('gtalug.apps.search.urls')),
	
	url(r'^(?P<prefix>%s)(?P<tiny>\w+)$' % '|'.join(settings.SHORTEN_MODELS.keys()),
		view  = 'shorturls.views.redirect'),
	url(r'^(?P<prefix>%s)(?P<tiny>\w+)/$' % '|'.join(settings.SHORTEN_MODELS.keys()),
		view  = 'shorturls.views.redirect'),
	
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
