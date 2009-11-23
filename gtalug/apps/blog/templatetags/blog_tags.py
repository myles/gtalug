import re
import datetime

from django import template
from django.db import models

Post = models.get_model('blog', 'post')

register = template.Library()

class BlogPostsPublished(template.Node):
	def __init__(self, limit, var_name):
		self.limit = limit
		self.var_name = var_name
	
	def render(self, context):
		posts = Post.objects.published()[:int(self.limit)]
		
		if posts and (int(self.limit) == 1):
			context[self.var_name] = posts[0]
		else:
			context[self.var_name] = posts
		
		return ''

@register.tag
def get_blog_posts_published(parser, token):
	"""Gets the upcoming meetings.
	
	Syntax::
		
		{% get_blog_posts_published [limit] as [var_name] %}
	
	Example usage::
		
		{% get_blog_posts_published 4 as upcoming_meetings %}
	"""
	try:
		tag_name, arg = token.contents.split(None, 1)
	except ValueError:
		raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
	
	m = re.search(r'(.*?) as (\w+)', arg)
	
	if not m:
		raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
	
	format_string, var_name = m.groups()
	
	return BlogPostsPublished(format_string, var_name)