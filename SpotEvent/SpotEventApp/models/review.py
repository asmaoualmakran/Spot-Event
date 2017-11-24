from django.db import models
from SpotEventApp.models.user import User
from SpotEventApp.models.venue import Venue
from SpotEventApp.models.identifier import Identifier

class Review(models.Model):
	user_id		= models.ForeignKey(User)
	venue_id	= models.ForeignKey(Venue)
	score		= models.IntegerField() #before we let the user give a score we need to check wether it is in the range
	review 		= models.TextField()


def __str__(self):
	return '%s' %(self.review)
