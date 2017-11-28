from django.db import models
from SpotEventApp.models.user import User
from SpotEventApp.models.venue import Venue

#%(app_label)s_%(class)s_ is needed to avoid name clashes of different classes

class Review(models.Model):
	user_id		= models.ForeignKey(User, related_name='%(app_label)s_%(class)s_user', null=True, on_delete=models.SET_NULL)
	venue_id	= models.ForeignKey(Venue, related_name='%(app_label)s_%(class)s_venue', null=True, on_delete=models.SET_NULL)
	score		= models.IntegerField() #before we let the user give a score we need to check wether it is in the range
	review 		= models.TextField()


