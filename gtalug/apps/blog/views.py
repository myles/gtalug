from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from gtalug.apps.blog.models import Post

def index(request, page=None):
	post_list = Post.objects.published()
	paginator = Paginator(post_list, 2)
	
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
	
	return render_to_response('blog/list.html', context,
			context_instance=RequestContext(request))

def detail(request, pk, slug=None):
	try:
		if slug:
			post = Post.objects.get(pk__exact=pk, slug__iexact=slug)
		else:
			post = Post.objects.get(pk__exact=pk)
	except Post.DoesNotExist:
		raise Http404
	
	context = {
		'post': post,
	}
	
	return render_to_response('blog/detail.html', context,
		context_instance=RequestContext(request))