import datetime

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatewords

from gtalug.apps.meetings.managers import MeetingManager

class Meeting(models.Model):
	"""
	A GTALUG meeting.
	"""
	topic = models.CharField('topic', max_length=255)
	slug = models.SlugField('slug', max_length=25)
	
	date = models.DateField('date', unique=True)
	time = models.TimeField('time', default=datetime.time(19, 30, 00))
	tba = models.BooleanField('TBA', default=False, help_text='To be announced')
	
	tease = models.TextField('tease', max_length=1000, help_text="Raw HTML")
	body = models.TextField('body', blank=True, null=True, help_text="Raw HTML")
	
	presenter = models.CharField('presenter', max_length=200)
	presenter_user = models.ForeignKey(User, verbose_name='presenters user account', blank=True, null=True)
	
	date_added = models.DateTimeField('date added', auto_now_add=True)
	date_modified = models.DateTimeField('date modified', auto_now=True)
	
	objects = MeetingManager()
	
	class Meta:
		verbose_name = 'meeting'
		verbose_name_plural = 'meetings'
		ordering = ('-date', '-time', 'topic')
		db_table = 'meetings'
	
	def __unicode__(self):
		return u"[%s-%s] %s" % (self.date.year, self.date.strftime('%m'), self.topic)
	
	@models.permalink
	def get_absolute_url(self):
		return ('meetings_detail', None, {
			'slug': self.slug,
			'year': self.date.year,
			'month': self.date.strftime('%m')
		})