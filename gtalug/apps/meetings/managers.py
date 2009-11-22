import datetime
import operator

from django.db.models import Manager, Q

class MeetingManager(Manager):
	
	def upcoming(self):
		"""Upcoming meetings.
		"""
		return self.get_query_set().filter(date__gte=datetime.date.today()).order_by('date')
	
	def upcoming_not_tba(self):
		"""Upcoming meetings that are not to be announced.
		"""
		return self.get_query_set().filter(date__gte=datetime.date.today(), tba=False).order_by('date')
	
	def past(self):
		"""Meeting in the past.
		"""
		return self.get_query_set().filter(date__lte=datetime.date.today()).order_by('-date')
	
	def eight_days(self):
		"""Upcoming meetings 8 days in the future.
		"""
		return self.get_query_set().filter(date__lte=datetime.date.today() + datetime.timedelta(8))
	
	def all_not_tba(self):
		"""All meetings that are not to be announced.
		"""
		return self.get_query_set().filter(tba__isnull=True).order_by('date')
	
	def search(self, search_terms):
		"""Simple search.
		"""
		terms = [term.strip() for term in search_terms.split()]
		q_objects = []
		
		for term in terms:
			q_objects.append(Q(topic__icontains=term))
			q_objects.append(Q(tease__icontains=term))
			q_objects.append(Q(body__icontains=term))
		
		qs = self.get_query_set()
		return qs.filter(reduce(operator.or_, q_objects))