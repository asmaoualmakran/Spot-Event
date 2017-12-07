from django.db import models
from SpotEventApp.models.identifier import Identifier

class Venue(Identifier):
	venue_name = models.CharField(max_length=30)



