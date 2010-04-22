import datetime

import vobject

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.defaultfilters import striptags
from django.http import Http404, HttpResponseRedirect, HttpResponse

from gtalug.apps.meetings.models import Meeting

def list(request, year=None):
	"""List meetings page.
	"""
	if not year:
		year = datetime.datetime.now().year
	
	meetings = Meeting.objects.all_not_tba(date__year=year)
	
	context = {
		'meetings': meetings,
		'year': year
	}
	
	return render_to_response('meetings/list.html', context,
		context_instance=RequestContext(request))

def next(request):
	"""Redirect to the next meeting.
	"""
	meeting = Meeting.objects.upcoming()[0]
	return HttpResponseRedirect(meeting.get_absolute_url())

def detail(request, year, month, slug=None):
	"""Meeting detail page.
	"""
	try:
		if slug:
			meeting = Meeting.objects.get(slug__iexact=slug, date__year=year, date__month=month)
		else:
			meeting = Meeting.objects.get(date__year=year, date__month=month)
	except Meeting.DoesNotExist:
		raise Http404
	
	context = {
		'meeting': meeting,
	}
	
	return render_to_response('meetings/detail.html', context,
		context_instance=RequestContext(request))

def ical(request):
	"""Meetings iCal (ics) feed.
	"""
	meetings = Meeting.objects.upcoming()
	
	cal = vobject.iCalendar()
	
	cal.add('method').vaule = u'PUBLISHED'
	cal.add('x-wr-calname').value = u"GTALUG"
	
	for meeting in meetings:
		vevent = cal.add('vevent')
		
		if meeting.tba:
			vevent.add('summary').value = u"GTALUG Meeting"
		else:
			vevent.add('summary').value = u"GTALUG Meeting - %s" % meeting.topic
			vevent.add('description').value = u"%s" % striptags(meeting.tease).strip()
		
		vevent.add('location').value = u"%s" % striptags(meeting.location).strip()
		vevent.add('dtstart').value = datetime.datetime.combine(meeting.date, meeting.time)
		vevent.add('url').value = u'http://gtalug.org%s' % meeting.get_absolute_url()
	
	icalstream = cal.serialize()
	
	response = HttpResponse(icalstream, mimetype='text/calendar')
	response['Filename'] = 'gtalug.ics'  # Fucking IE needs this
	response['Content-Disposition'] = 'attachment; filename=gtalug.ics'
	
	return response