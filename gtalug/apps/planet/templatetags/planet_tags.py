import re
import datetime

from django import template
from django.db import models

Feed = models.get_model('planet', 'feed')
Post = models.get_model('planet', 'post')

register = template.Library()

class PlanetFeeds(template.Node):
	def __init__(self, var_name):
		self.var_name = var_name
	
	def render(self, context):
		feeds = Feed.objects.filter(is_active=True)
		
		context[self.var_name] = feeds
		
		return ''

@register.tag
def get_planet_feeds(parser, token):
	"""Gets the planets feeds
	
	Syntax::
		
		{% get_planet_feeds [var_name] %}
	
	Example usage::
		
		{% get_planet_feeds feeds %}
	"""
	try:
		tag_name, args = token.contents.split()
	except ValueError:
		raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
	
	return PlanetFeeds(args)

class PlanetPosts(template.Node):
	def __init__(self, limit, var_name):
		self.limit = limit
		self.var_name = var_name

	def render(self, context):
		posts = Post.objects.all()[:int(self.limit)]

		if posts and (int(self.limit) == 1):
			context[self.var_name] = posts[0]
		else:
			context[self.var_name] = posts

		return ''

@register.tag
def get_planet_posts(parser, token):
	"""Gets the published posts.

	Syntax::

		{% get_planet_posts [limit] as [var_name] %}

	Example usage::

		{% get_planet_posts 4 as upcoming_meetings %}
	"""
	try:
		tag_name, arg = token.contents.split(None, 1)
	except ValueError:
		raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]

	m = re.search(r'(.*?) as (\w+)', arg)

	if not m:
		raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name

	format_string, var_name = m.groups()

	return PlanetPosts(format_string, var_name)