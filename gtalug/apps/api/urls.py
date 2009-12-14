from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication

from gtalug.apps.blog.handlers import PostListHandler, PostDetailHandler

blog_post_list_resource = Resource(handler=PostListHandler)
blog_post_detail_resource = Resource(handler=PostDetailHandler)

from gtalug.apps.meetings.handlers import MeetingListHandler, MeetingDetailHandler, MeetingNextHandler

meeting_list_resource = Resource(handler=MeetingListHandler)
meeting_detail_resource = Resource(handler=MeetingDetailHandler)
meeting_next_resource = Resource(handler=MeetingNextHandler)

urlpatterns = patterns('',
	url(r'^blog\.(?P<emitter_format>.+)$', blog_post_list_resource),
	url(r'^blog/(?P<pk>\d+)-(?P<slug>[-\w]+)\.(?P<emitter_format>.+)$', blog_post_detail_resource),
	
	url(r'^meetings\.(?P<emitter_format>.+)$', meeting_list_resource),
	url(r'^meetings/(?P<year>\d{4})\.(?P<emitter_format>.+)$', meeting_list_resource),
	url(r'^meetings/(?P<year>\d{4})-(?P<month>\d{2})\.(?P<emitter_format>.+)$', meeting_next_resource),
	url(r'^meetings/(?P<year>\d{4})-(?P<month>\d{2})-(?P<slug>[-\w]+)\.(?P<emitter_format>.+)$', meeting_next_resource),
	url(r'^meetings/next\.(?P<emitter_format>.+)$', meeting_next_resource)
)