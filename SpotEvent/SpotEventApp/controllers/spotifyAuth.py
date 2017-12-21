from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SpotEventApp import config
from django.shortcuts import redirect
from django.http import HttpRequest 
from SpotEventApp.serializers.spotifyAuth import Create_spotifyAuth as Create_spotifyAuthSerializer
from SpotEventApp.serializers.spotifyAuth import SpotifyAuth as SpotifyAuthSerializer
from SpotEventApp.models.spotifyAuth import spotifyAuth as spotifyAuthModel
import base64, requests, json
from rest_framework.reverse import reverse

# When user surfs to /login, the user will be redirected 
#to the autorize_link defined in the config
@api_view(['GET'])
def login(request):
	return redirect(config.authorize_link)


# create the authorisation link 
@api_view(['GET'])
def request_Auth(request):
	user_id = int(request.COOKIES['id'])
	# format={'pk':user_id}
	# user_id = reverse('api:user-detail', request=request, kwargs=format)
	code = request.GET.get('code') #we querry out the code, we need this for the post request back to Spotify API 
	request_link = requests.post(config.token_link, data={'code': code, 'grant_type': 'authorization_code', 'redirect_uri': 'http://127.0.0.1:8000/authed', 'client_id': config.PUBLIC_KEY, 'client_secret': config.PRIVATE_KEY})
	content = json.loads(request_link.content.decode('utf-8'))
	content['user_id'] = user_id
	serializer = Create_spotifyAuthSerializer(data=content)
	if (serializer.is_valid()):
		auth = serializer.save()
		serializer = SpotifyAuthSerializer(auth, context={'request':request})
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	else:
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return Response(content)

#token_link, we send a request to this link 

@api_view(['GET', 'PUT', 'DELETE'])
def single_spotifyAuth_request(request, pk):
	try:
		spotifyAuth = spotifyAuthModel.objects.get(id=pk)
	except spotifyAuth.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if(request.method == 'GET'):
		serializer = SpotifyAuthSerializer(spotifyAuth, context={'request':request})
		return Response(serializer.data, status=status.HTTP_200_OK)

	elif(request.method == 'PUT'):
		serializer = SpotifyAuthSerializer(spotifyAuth, data=request.data, content={'request':request})
		if(serializer.is_valid()):
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	else:
		spotifyAuth.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)	

@api_view(['GET'])
def refresh_token(request, pk):
	try:
		spotifyAuth = spotifyAuthModel.objects.get(id=pk)
	except spotifyAuth.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	refresh_token = spotifyAuth.refresh_token
	request_link = requests.post(config.token_link, data={'grant_type': 'refresh_token', 'refresh_token': refresh_token, 'client_id': config.PUBLIC_KEY, 'client_secret': config.PRIVATE_KEY})
	content = json.loads(request_link.content.decode('utf-8'))
	serializer = SpotifyAuthSerializer(spotifyAuth, data=content, context={'request':request})
	if(serializer.is_valid()):
		serializer.save()
		return  Response(serializer.data, status=status.HTTP_201_CREATED)
	else:
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
