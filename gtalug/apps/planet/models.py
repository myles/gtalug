from django.db import models
from django.contrib.auth.models import User

class Feed(models.Model):
	feed_url = models.URLField('feed url', unique=True)
	
	name = models.CharField('name', max_length=100)
	shortname = models.CharField('shortname', max_length=25)
	is_active = models.BooleanField('is active', default=True,
		help_text='If disabled, this feed will not be further updated.')
	user = models.ForeignKey(User, blank=True, null=True)
	
	title = models.CharField('title', max_length=200, blank=True)
	tagline = models.TextField('tagline', blank=True)
	link = models.URLField('link', blank=True)
	
	# http://feedparser.org/docs/http-etag.html
	etag = models.CharField(_('etag'), max_length=50, blank=True)
	last_modified = models.DateTimeField(_('last modified'), null=True, blank=True)
	last_checked = models.DateTimeField(_('last checked'), null=True, blank=True)
	
	date_added = models.DateTimeField('date added', auto_now_add=True)
	date_modified = models.DateTimeField('date modified', auto_now=True)
	
	class Meta:
		db_table = 'planet_feeds'
		verbose_name = 'feed'
		verbose_name_plural = 'feeds'
		ordering = ('name', 'feed_url')
	
	def __unicode__(self):
		return u"%s (%s)" % (self.name, self.feed_url)
	
	def get_absolute_url(self):
		return self.link

class Post(models.Model):
	feed = models.ForeignKey(Feed, verbose_name='feed')
	
	title = models.CharField('title', max_length=255)
	link = models.URLField('link')
	content = models.TextField('content', blank=True)
	
	guid = models.CharField('guid', max_length=200, db_index=True)
	author = models.CharField('author', max_length=50, blank=True)
	author_email = models.EmailField('author email', blank=True)
	
	date_modified = models.DateTimeField('date modified', null=True, blank=True)
	date_added = models.DateField('date added', auto_now_add=True)
	
	class Meta:
		db_table = 'planet_posts'
		verbose_name = 'post'
		verbose_name_plural = 'posts'
		ordering = ('-date_modified')
		unique_together = (('feed', 'guid'),)
	
	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return self.link