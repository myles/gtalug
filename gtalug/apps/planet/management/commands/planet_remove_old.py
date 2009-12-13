import datetime

from django.core.management.base import BaseCommand
from django.db import models

class Command(BaseCommand):
	def handle(self, *args, **options):
		Post = models.get_model('planet', 'post')
		
		posts = Post.objects.filter(date_modified__lt=
			datetime.datetime.now() - datetime.timedelta(days=90))
		
		for p in posts: p.delete()
		
		return "Deleted %s posts" % posts.count()