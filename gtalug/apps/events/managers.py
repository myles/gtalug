import datetime

from django.db.models import Manager

class EventManager(Manager):
	
	def published(self):
		"""Published events."""
		return self.get_query_set().filter(
			date__gte=datetime.date.today()).order_by('-date')
