from django.db import models
from SpotEventApp.user import User

#TODO: Writen user authentication
# this is the athentication for the spotify accounts
# this will hold the tokens for the accounts
#class Authentication(models.Model):
#	user_id =  models.ForeignKey(User, related_name='%(app_label)s_%(class)s_user', null=True, on_delete=models.SET_NULL)
#	spotify_token = models.


class spotifyAuth(models.Model):
	user_id 				= models.ForeignKey(User, related_name='%(app_label)s_%(class)s_user', null=True, on_delete=models.SET_NULL)
	spotify_acces_token 	= models.CharField(max_lenght=200)  #we're saving the spotify token as a string
	spotify_refresh_token 	= models.CharField(max_length=200)