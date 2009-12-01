import urlparse
from django import template
from django.conf import settings
from django.core import urlresolvers
from django.utils.safestring import mark_safe

class FullURL(template.Node):
	@classmethod
	def parse(cls, parser, token):
		parts = token.split_contents()
		
		if len(parts) != 2:
			raise template.TemplateSyntaxError("%s takes exactly one argument" % parts[0])
		
		return cls(template.Variable(parts[1]))
	
	def __init__(self, obj):
		self.obj = obj
	
	def render(self, context):
		try:
			obj = self.obj.resolve(context)
		except template.VariableDoesNotExist:
			return ''
		
		if hasattr(settings, 'SHORTEN_FULL_BASE_URL') and settings.SHORTEN_FULL_BASE_URL:
			return urlparse.urljoin(settings.SHORTEN_FULL_BASE_URL, obj.get_absolute_url())
		else:
			return obj.get_absolute_url()

register = template.Library()
register.tag('fullurl', FullURL.parse)