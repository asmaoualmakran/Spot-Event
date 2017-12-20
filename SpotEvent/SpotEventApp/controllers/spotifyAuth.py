from rest_framework.decorators import api_view
from SpotEventApp import config
from django.shortcuts import redirect
import base64


# When user surfs to /login, the user will be redirected 
#to the autorize_link defined in the config
@api_view(['GET'])
def login(request):
	return redirect(config.authorize_link)


# create the authorisation link 
@api_view(['POST'])
def request_Auth(request):
	code = requests.query['code']
	request_link = requests.request(token_link, data={'code': code, 'grant_type': 'authorisation_code', 'redirect_uri': 'http://127.0.0.1:8080/authed', 'client_id': PUBLIC_KEY, 'client_secret': SECRET_KEY})
	return request_link.content




#def refresh_token():
