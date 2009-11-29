import re
import datetime

from django import template
from django.db import models

Event = models.get_model('events', 'event')

register = template.Library()

class EventsPublished(template.Node):
	def __init__(self, limit, var_name):
		self.limit = limit
		self.var_name = var_name
	
	def render(self, context):
		posts = Event.objects.published()[:int(self.limit)]
		
		if posts and (int(self.limit) == 1):
			context[self.var_name] = posts[0]
		else:
			context[self.var_name] = posts
		
		return ''

@register.tag
def get_events_published(parser, token):
	"""Gets the upcoming events.
	
	Syntax::
		
		{% get_events_published [limit] as [var_name] %}
	
	Example usage::
		
		{% get_events_published 4 as upcoming_meetings %}
	"""
	try:
		tag_name, arg = token.contents.split(None, 1)
	except ValueError:
		raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
	
	m = re.search(r'(.*?) as (\w+)', arg)
	
	if not m:
		raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
	
	format_string, var_name = m.groups()
	
	return EventsPublished(format_string, var_name)