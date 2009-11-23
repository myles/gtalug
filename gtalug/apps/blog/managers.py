from datetime import datetime
import operator

from django.db.models import Manager, Q

class BlogPostManager(Manager):
	
	def published(self):
		"""Published blog posts.
		"""
		return self.get_query_set().filter(published__gte=datetime.now()).order_by('-published')
	
	def search(self, search_terms):
		"""Simple search.
		"""
		terms = [term.strip() for term in search_terms.split()]
		q_objects = []
		
		for term in terms:
			q_objects.append(Q(title__icontains=term))
			q_objects.append(Q(tease__icontains=term))
			q_objects.append(Q(body__icontains=term))
		
		qs = self.get_query_set()
		return qs.filter(reduce(operator.or_, q_objects))