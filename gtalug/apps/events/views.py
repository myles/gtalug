import datetime
import time

from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

from gtalug.apps.events.models import Event
from gtalug.apps.meetings.models import Meeting

def list(request, year=None, month=None):
	TODAY = datetime.date.today()
	
	if not year and not month:
		year = TODAY.year
		month = TODAY.strftime('%m')
	
	try:
		tt = time.strptime("%s-%s" % (year, month), '%s-%s' % ('%Y', '%m'))
		date = datetime.date(*tt[:3])
	except ValueError:
		raise Http404
	
	first_day = date.replace(day=1)
	if first_day.month == 12:
		last_day = first_day.replace(year=first_day.year + 1, month=1)
	else:
		last_day = first_day.replace(month=first_day.month + 1)
	
	events = Event.objects.filter(date__gte=first_day, date__lt=last_day)
	
	# Calculate the next month, if applicable.
	if last_day <= datetime.date.today():
		next_month = last_day
	else:
		next_month = last_day
	
	# Calculate the previous month
	if first_day.month == 1:
		previous_month = first_day.replace(year=first_day.year-1,month=12)
	else:
		previous_month = first_day.replace(month=first_day.month-1)
	
	try:
		meeting = Meeting.objects.get(date__year=year, date__month=month)
	except Meeting.DoesNotExist:
		meeting = None
	
	context = {
		'events': events,
		'date': date,
		'meeting': meeting,
		'previous_month': previous_month,
		'next_month': next_month
	}
	
	return render_to_response('events/list.html', context,
		context_instance=RequestContext(request))

def detail(request, year, month, pk, slug=None):
	try:
		if slug:
			event = Event.objects.get(pk__exact=pk, slug__iexact=slug, date__year=year, date__month=month)
		else:
			event = Event.objects.get(slug__iexact=slug, date__year=year, date__month=month)
	except Event.DoesNotExist:
		raise Http404
	
	context = {
		'event': event,
	}
	
	return render_to_response('events/detail.html', context,
		context_instance=RequestContext(request))