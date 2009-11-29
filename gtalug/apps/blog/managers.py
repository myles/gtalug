import datetime

from django.db.models import Manager

class BlogPostManager(Manager):
	
	def published(self):
		"""Published blog posts.
		"""
		return self.get_query_set().filter(
			published__lte=datetime.datetime.now()).order_by('-published')