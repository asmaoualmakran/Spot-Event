from django.db import models
from . import user
from . import venue
from . import identifier

class Review(models.Model):
	user_id		= models.ForeignKey(user.User)
	venue_id	= models.ForeignKey(venue.Venue)
	score		= models.IntegerField() #before we let the user give a score we need to check wether it is in the range
	review 		= models.CharField(max_length = 140)


def __str__(self):
	return '%s' %(self.review)
