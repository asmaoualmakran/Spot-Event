from django.db import models
from SpotEventApp.models.user import User

#TODO: Writen user authentication
# this is the athentication for the spotify accounts
# this will hold the tokens for the accounts
#class Authentication(models.Model):
#	user_id =  models.ForeignKey(User, related_name='%(app_label)s_%(class)s_user', null=True, on_delete=models.SET_NULL)
#	spotify_token = models.


class spotifyAuth(models.Model):
	user_id 				= models.ForeignKey(User, related_name='%(app_label)s_%(class)s_user', null=True, on_delete=models.SET_NULL)
	access_token 			= models.CharField(max_length=500, null=True)  #we're saving the spotify token as a string
	refresh_token 			= models.CharField(max_length=200, null=True)