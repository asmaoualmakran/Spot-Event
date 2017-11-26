from django.db import models
from SpotEventApp.models.venue import Venue
from SpotEventApp.models.user import User

class Event(models.Model):
	venue_id	= models.ForeignKey(Venue, related_name='%(app_label)s_%(class)s_venue')
	user_id		= models.ForeignKey(User, related_name='%(app_label)s_%(class)s_user')
	event_name	= models.CharField(max_length=30)
	event_date	= models.DateField()
	artists 	= models.CharField(max_length=100, default='NO_ARTISTS')
	genre 		= models.CharField(max_length=100, default='NO_GENRE')


#TODO: Enable for the event creator to add pictures of/for the event.
