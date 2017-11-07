from django.db import models
from . import venue

class Event(models.Model):
	venue_id	= models.ForeignKey(venue.Venue)
	event_name	= models.CharField(max_length=30)
	artists = models.CharField(max_length=100, default='NO_ARTISTS')

def __str__(self):
	return '%s' %(self.event_name)