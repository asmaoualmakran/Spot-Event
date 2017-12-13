from django.shortcuts import HttpResponse
from django.template.loader import get_template

# Create your views here.

def index(request):
	context = {}
	return HttpResponse(get_template('index.html').render(context, request))
