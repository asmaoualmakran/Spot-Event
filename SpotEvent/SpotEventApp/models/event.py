from django.db import models
from SpotEventApp.models.venue import Venue

class Event(models.Model):
	venue_id	= models.ForeignKey(Venue, related_name='venue')
	event_name	= models.CharField(max_length=30)
	artists = models.CharField(max_length=100, default='NO_ARTISTS')

	#add pictures
	
#def __str__(self):
#	return '%s' %(self.event_name)