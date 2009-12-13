import datetime

from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

from gtalug.apps.events.models import Event

def list(request, year=None, month=None):
	TODAY = datetime.date.today()
	
	if not year and not month:
		year = TODAY.year
		month = TODAY.strftime('%m')
	
	events = Event.objects.all()
	
	context = {
		'events': events,
		'year': year,
		'month': month
	}
	
	return render_to_response('events/list.html', context,
		context_instance=RequestContext(request))

def detail(request, year, month, slug):
	
	context = {}
	
	return render_to_response('events/detail.html', context,
		context_instance=RequestContext(request))