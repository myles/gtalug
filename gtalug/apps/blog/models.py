from django.db import models
from django.contrib.auth.models import User

from gtalug.apps.blog.managers import BlogPostManager

class Post(models.Model):
	title = models.CharField('title', max_length=255)
	slug = models.SlugField('slug', max_length=25)
	
	author = models.ForeignKey(User, verbose_name='author')
	published = models.DateTimeField('published', blank=True, null=True)
	
	tease = models.TextField('tease', max_length=1000, help_text="Raw HTML")
	body = models.TextField('body', blank=True, null=True, help_text="Raw HTML")
	
	date_added = models.DateTimeField('date added', auto_now_add=True)
	date_modified = models.DateTimeField('date modified', auto_now=True)
	
	objects = BlogPostManager()
	
	class Meta:
		verbose_name = 'post'
		verbose_name_plural = 'posts'
		db_table = 'blog_posts'
		ordering = ('-published',)
	
	def __unicode__(self):
		return u"%s" % self.title
	
	@models.permalink
	def get_absolute_url(self):
		return ('blog_post_detail', None, {
			'pk': self.pk,
			'slug': self.slug
		})