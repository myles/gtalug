from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from gtalug.apps.planet.models import Feed, Post

def index(request, page=None):
	post_list = Post.objects.all()
	paginator = Paginator(post_list, 20)
	
	if not page:
		try:
			page = int(request.GET.get('page', '1'))
		except ValueError:
			page = 1
	
	try:
		posts = paginator.page(page)
	except (EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)
	
	context = {
		'posts': posts,
	}
	
	return render_to_response('planet/list.html', context,
			context_instance=RequestContext(request))

def feed_detail(request, slug):
	try:
		feed = Feed.objects.get(slug__iexact=slug)
	except Feed.DoesNotExist:
		raise Http404
	
	context = {
		'feed': feed,
	}
	
	return render_to_response('planet/feed_detail.html', context,
		context_instance=RequestContext(request))

def post_detail(request, slug, pk):
	try:
		feed = Feed.objects.get(slug__iexact=slug)
	except Feed.DoesNotExist:
		raise Http404
	
	try:
		post = Post.objects.get(pk=pk)
	except Post.DoesNotExist:
		raise Http404
	
	context = {
		'feed': feed,
		'post': post,
	}
	
	return render_to_response('planet/post_detail.html', context,
		context_instance=RequestContext(request))