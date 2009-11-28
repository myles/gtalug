from haystack import indexes
from haystack import site

from gtalug.apps.blog.models import Post

class PostIndex(indexes.SearchIndex):
	text = indexes.CharField(document=True, use_template=True)
	date = indexes.DateField(model_attr='published')
	user = indexes.CharField(model_attr='author')
	title = indexes.CharField(model_attr='title')
	content = indexes.CharField(model_attr='tease')
		
	def get_queryset(self):
		return Post.objects.published()

site.register(Post, PostIndex)