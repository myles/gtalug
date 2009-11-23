from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

from gtalug.apps.meetings.models import Meeting

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