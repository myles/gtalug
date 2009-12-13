from re import escape

from django.contrib import admin
from django.conf import settings
from django.conf.urls.defaults import *

from gtalug.apps.meetings.feeds import RssMeetingFeed, AtomMeetingFeed
from gtalug.apps.blog.feeds import RssPostFeed, AtomPostFeed

from gtalug.apps.meetings.sitemaps import MeetingSitemap
from gtalug.apps.blog.sitemaps import PostSitemap

admin.autodiscover()

handler404 = 'perfect404.views.page_not_found'

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
	url(r'^planet/', include('gtalug.apps.planet.urls')),
	url(r'^events/', include('gtalug.apps.events.urls')),
	
	url(r'^search/', include('gtalug.apps.search.urls')),
	
	# ShortURLs
	url(r'^(?P<prefix>%s)(?P<tiny>\w+)$' % '|'.join(settings.SHORTEN_MODELS.keys()),
		view  = 'shorturls.views.redirect'),
	url(r'^(?P<prefix>%s)(?P<tiny>\w+)/$' % '|'.join(settings.SHORTEN_MODELS.keys()),
		view  = 'shorturls.views.redirect'),
	
	# Syndication
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
	
	# Sitemap XML
	url(r'^sitemap.xml$',
		'django.contrib.sitemaps.views.sitemap',
		{ 'sitemaps': sitemaps }
	),
	
	# Django Stuff.
	url(r'^comments/', include('django.contrib.comments.urls')),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^%s/(.*)$' % escape(settings.MEDIA_URL.strip('/')),
			'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
	)