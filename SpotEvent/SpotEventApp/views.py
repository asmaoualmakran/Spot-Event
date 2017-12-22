from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect
from rest_framework.reverse import reverse

def login(request):
	context={}
	return HttpResponse(get_template('login.html').render(context, request))

def profile(request):
	if('id' not in request.COOKIES):
		return redirect(reverse('login', request=request))
	context={}
	return HttpResponse(get_template('profile.html').render(context, request))

def event(request, pk):
	if('id' not in request.COOKIES):
		return redirect(reverse('login', request=request))
	context={}
	return HttpResponse(get_template('event.html').render(context, request))

def ticketevent(request, pk):
	if('id' not in request.COOKIES):
		return redirect(reverse('login', request=request))
	context={}
	return HttpResponse(get_template('ticketevent.html').render(context, request))

def review(request):
	if('id' not in request.COOKIES):
		return redirect(reverse('login', request=request))
	context={}
	return HttpResponse(get_template('review.html').render(context, request))

def venue(request):
	if('id' not in request.COOKIES):
		return redirect(reverse('login', request=request))
	context={}
	return HttpResponse(get_template('venue.html').render(context, request))

def address(request):
	if('id' not in request.COOKIES):
		return redirect(reverse('login', request=request))
	context={}
	return HttpResponse(get_template('address.html').render(context, request))

def browse(request):
	if('id' not in request.COOKIES):
		return redirect(reverse('login', request=request))
	context={}
	return HttpResponse(get_template('browse.html').render(context, request))

def spotlight(request):
	if('id' not in request.COOKIES):
		return redirect(reverse('login', request=request))
	context={}
	return HttpResponse(get_template('spotlight.html').render(context, request))

def addevent(request):
	if('id' not in request.COOKIES):
		return redirect(reverse('login', request=request))
	context={}
	return HttpResponse(get_template('addevent.html').render(context, request))

def search(request,pk):
	if('id' not in request.COOKIES):
		return redirect(reverse('login', request=request))
	context={}
	return HttpResponse(get_template('search.html').render(context,request))

