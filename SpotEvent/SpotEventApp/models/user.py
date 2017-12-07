from django.db import models
from SpotEventApp.models.identifier import Identifier

class User(Identifier):
	username 	= models.CharField(max_length=30) # the username may contain alphanumeric, _, @, +, . and - characters
	first_name 	= models.CharField(max_length=30)
	last_name 	= models.CharField(max_length=30)
	birthday 	= models.DateField()
	email 		= models.EmailField()
	
