from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect

from gtalug.apps.profiles.models import Profile

def detail(request, username):
	try:
		user = User.objects.get(username=username)
		profile = Profile.objects.get(user=user)
	except User.DoesNotExist and Profile.DoesNotExist:
		raise Http404
	
	context = {
		'user': user,
		'profile': profile,
	}
	
	return render_to_response('profiles/detail.html', context,
		context_instance=RequestContext(request))