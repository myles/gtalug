from django import template
from django.db import models

import re

Meeting = models.get_model('meetings', 'meeting')

register = template.Library()

class UpcomingMeetings(template.Node):
	def __init__(self, limit, var_name):
		self.limit = limit
		self.var_name = var_name
	
	def render(self, context):
		meetings = Meeting.objects.upcoming()[:int(self.limit)]
		
		if meetings and (int(self.limit) == 1):
			context[self.var_name] = meetings[0]
		else:
			context[self.var_name] = meetings
		
		return ''

@register.tag
def get_upcoming_meetings(parser, token):
	"""Gets the upcoming meetings.
	
	Syntax::
		
		{% get_upcoming_meetings [limit] as [var_name] %}
	
	Example usage::
		
		{% get_upcoming_meetings 4 as upcoming_meetings %}
	"""
	try:
		tag_name, arg = token.contents.split(None, 1)
	except ValueError:
		raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
	
	m = re.search(r'(.*?) as (\w+)', arg)
	
	if not m:
		raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
	
	format_string, var_name = m.groups()
	
	return UpcomingMeetings(format_string, var_name)