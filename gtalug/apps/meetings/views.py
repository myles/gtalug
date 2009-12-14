import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect

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