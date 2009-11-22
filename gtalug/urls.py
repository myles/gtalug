from re import escape

from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$',
		'django.views.generic.simple.direct_to_template',
		{'template': 'index.html'},
		'homepage',
	),
	
	url(r'^meetings/', include('gtalug.apps.meetings.urls')),
	
	(r'^search/', include('haystack.urls')),
	
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	
	url(r'^%s/(.*)$' % escape(settings.MEDIA_URL.strip('/')),
		'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
)
