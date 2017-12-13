from django.http import HttpResponse
from django.template.loader import get_template

def index(request):
	context={}
	return HttpResponse(get_template('User.html').render(context, request))
