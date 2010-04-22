import datetime

from django.core.management.base import BaseCommand
from django.db import models

class Command(BaseCommand):
	def handle(self, *args, **options):
		Meeting = models.get_model('meetings', 'meeting')
		earliest_meeting = Meeting.objects.all().order_by('-date')[0]
		
		dtstart = earliest_meeting.date + datetime.timedelta(days=1)
		
		from dateutil.rrule import rrule, MONTHLY, TU
		
		months = list(rrule(MONTHLY, count=12, dtstart=dtstart, byweekday=TU(2)))
		
		default_topic = 'To be announced'
		default_slug = 'tba'
		default_time = datetime.time(19, 30, 00)
		default_tease = '<p>To be announced</p>'
		default_location = '<p>\nRoom GB248, Galbraith Building, University of Toronto\n<br>35 St George St<br>\nToronto, Ontario M5S 3G8<br>\nUniversity of Toronto\n</p>'
		default_presenter = 'TBA'
		
		for month in months:
			print "Adding meeting for %s %s" % (month.strftime('%m'), month.year)
			Meeting.objects.create(topic=default_topic, slug=default_slug, time=default_time, tease=default_tease, location=default_location, presenter=default_presenter, tba=True, date=month)