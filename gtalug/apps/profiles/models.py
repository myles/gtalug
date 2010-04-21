import datetime

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	"""
	A GTALUGer's Profile.
	"""
	user = models.ForeignKey(User, verbose_name='User account', unique=True)
	
	bio = models.TextField('Biography', blank=True, null=True)
	birthday = models.DateField('Birthday', blank=True, null=True)
	
	photo = models.ImageField('Photo', blank=True, null=True, upload_to='profiles')
	
	date_added = models.DateTimeField('date added', auto_now_add=True)
	date_modified = models.DateTimeField('date modified', auto_now=True)
	
	class Meta:
		verbose_name = 'profile'
		verbose_name_plural = 'profiles'
		ordering = ('user__username',)
		db_table = 'profiles'
	
	@property
	def get_name(self):
		if self.user.first_name and self.user.last_name:
			return u"%s %s." % (
				self.user.first_name.title(),
				self.user.last_name[0].upper())
		elif self.user.first_name:
			return u"%s" % self.user.first_name
		else:
			return u"%s" % self.user.username
	
	def __unicode__(self):
		return self.get_name
	
	@models.permalink
	def get_absolute_url(self):
		return ('profiles_detail', None, {
			'username': self.user.username,
		})
	
	@property
	def age(self):
		TODAY = datetime.date.today()
		difference = TODAY - self.birthday
		return difference.days / 365