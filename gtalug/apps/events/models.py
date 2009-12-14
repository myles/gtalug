from django.db import models
from django.contrib.auth.models import User

from gtalug.apps.events.managers import EventManager

class Event(models.Model):
	title = models.CharField('title', max_length=200)
	slug = models.SlugField('slug', max_length=25)
	author = models.ForeignKey(User, verbose_name='author')
	
	date = models.DateField('date')
	time = models.TimeField('time', blank=True, null=True)
	
	tease = models.TextField('tease', max_length=1000, help_text="Raw HTML")
	body = models.TextField('body', blank=True, null=True, help_text="Raw HTML")
	
	date_added = models.DateTimeField('date added', auto_now_add=True)
	date_modified = models.DateTimeField('date modified', auto_now=True)
	
	objects = EventManager()
	
	class Meta:
		verbose_name = 'event'
		verbose_name_plural = 'events'
		db_table = 'events'
		ordering = ('-date',)
	
	def __unicode__(self):
		return u"%s" % self.title
	
	@models.permalink
	def get_absolute_url(self):
		return ('events_detail', None, {
			'slug': self.slug,
			'pk': self.pk,
			'year': self.date.year,
			'month': self.date.strftime('%m')
		})