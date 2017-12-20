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
	return redirect(config.authorize_link)


# create the authorisation link 
@api_view(['GET'])
def request_Auth(request):
	code = request.GET.get('code') #we querry out the code, we need this for the post request back to Spotify API 
	request_link = requests.post(config.token_link, data={'code': code, 'grant_type': 'authorization_code', 'redirect_uri': 'http://127.0.0.1:8000/authed', 'client_id': config.PUBLIC_KEY, 'client_secret': config.PRIVATE_KEY})
	content = request_link.content
	return Response(content)

#token_link, we send a request to this link 

#@api_view(['POST'])
#def refresh_token(request):



