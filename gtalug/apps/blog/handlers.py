from piston.handler import BaseHandler
from piston.utils import rc, throttle

from gtalug.apps.blog.models import Post

class PostListHandler(BaseHandler):
	allowed_methods = ('GET',)
	fields = ('title', 'slug', 'id', 'tease', 'body', 'published', ('author', ('username', 'first_name', 'last_name')))
	exclued = ('id',)
	model = Post
	
	def read(self, request):
		return Post.objects.published()

class PostDetailHandler(BaseHandler):
	allowed_methods = ('GET',)
	fields = ('title', 'slug', 'tease', 'body', 'published', ('author', ('username', 'first_name', 'last_name')), 'content_size')
	exclued = ('id',)
	model = Post
	
	@classmethod
	def content_size(self, post):
		return len(post.body)
	
	def read(self, request, pk, slug):
		return Post.objects.get(pk=pk, slug=slug)