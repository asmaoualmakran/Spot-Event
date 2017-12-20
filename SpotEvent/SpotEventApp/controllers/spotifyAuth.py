from rest_framework.decorators import api_view
from rest_framework.response import Response
from SpotEventApp import config
from django.shortcuts import redirect
from django.http import HttpRequest 
import base64, requests


# When user surfs to /login, the user will be redirected 
#to the autorize_link defined in the config
@api_view(['GET'])
def login(request):
	print('start login')
	return redirect(config.authorize_link)


# create the authorisation link 
@api_view(['GET'])
def request_Auth(request):
	print('test')
	print(request)
	code = request.GET.get('code') #we querry out the code, we need this for the post request back to Spotify API 
	print('code fetched')
	print(code)
	request_link = requests.post(config.token_link, data={'code': code, 'grant_type': 'authorisation_code', 'redirect_uri': 'http://127.0.0.1:8080/authed', 'client_id': config.PUBLIC_KEY, 'client_secret': config.PRIVATE_KEY})
	content = request_link.content
	print(request_link.content)
	return Response(content)

#token_link, we send a request to this link 

#@api_view(['POST'])
#def refresh_token(request):



