from rest_framework import serializers
from SpotEventApp.models.spotifyAuth import spotifyAuth as spotifyAuthModel


class SpotifyAuth(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta: 
		model = spotifyAuthModel
		fields = ('id', 'user_id', 'access_token', 'refresh_token')
	#	extra_kwargs = 'user_id':{'view_name': 'api:user-detail'}


class Create_spotifyAuth(serializers.ModelSerializer):

	class Meta: 
		model = spotifyAuthModel
		fields = ('user_id', 'access_token', 'refresh_token')