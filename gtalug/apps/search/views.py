from django.http import Http404, HttpResponse
from django.conf import settings
from django.utils import feedgenerator
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage

from haystack.forms import HighlightedModelSearchForm

from gtalug.apps.search.feeds import RssSearchFeed, AtomSearchFeed

RESULTS_PER_PAGE = getattr(settings, 'HAYSTACK_SEARCH_RESULTS_PER_PAGE', 20)

def search(request):
	query = ''
	results = []
	
	if request.GET.get('q'):
		form = HighlightedModelSearchForm(request.GET, None, load_all=True)
		
		if form.is_valid():
			query = form.cleaned_data['q']
			results = form.search()
	else:
		form = HighlightedModelSearchForm(None, load_all=True)
	
	paginator = Paginator(results, RESULTS_PER_PAGE)
	
	try:
		page = paginator.page(int(request.GET.get('page', 1)))
	except InvalidPage:
		raise Http404("Not such page of results!")
	
	if page.object_list:
		if request.GET.get('output') == 'rss':
			feed = feedgenerator.Rss201rev2Feed(title=u"GTALUG Search feed %s" % query,
				link=u"http://gtalug.org/", description="")
		elif request.GET.get('output') == 'atom':
			feed = feedgenerator.Atom1Feed(title=u"GTALUG Search feed %s" % query,
				link=u"http://gtalug.org/", description="")
		else:
			feed = None
		
		if feed:
			for result in page.object_list:
				feed.add_item(title=result.object,
					link=result.object.get_absolute_url(), description="")
				return HttpResponse(feed.writeString('UTF-8'), mimetype=feed.mime_type)
	
	context = {
		'form': form,
		'page': page,
		'paginator': paginator,
		'query': query,
	}
	
	return render_to_response('search/search.html', context,
		context_instance=RequestContext(request))