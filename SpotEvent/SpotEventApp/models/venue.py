from django.db import models
from . import address
from . import identifier

class Venue(identifier.Identifier):
	venue_name = models.CharField(max_length = 30)


def __str__(self):
	return '%s' % (self.venue_name,)
