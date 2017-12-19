from django.db import models
from SpotEventApp.models.venue import Venue
from SpotEventApp.models.user import User

class Event(models.Model):

		#This will upload the file to MEDIA_ROOT/ Event<id>/<filename>
	def media_directory_path(instance, filename):
		return 'event_{0}/{1}'.format(instance.Event.id, filename)

	#only paths to the images are saved in the DB, for peformance reasons 
	#The files are saved in /Spot-Event/SpotEvent/media, with the format used above

	venue_id	= models.ForeignKey(Venue, related_name='%(app_label)s_%(class)s_venue', null=True, on_delete=models.SET_NULL)
	user_id		= models.ForeignKey(User, related_name='%(app_label)s_%(class)s_user', null=True, on_delete=models.SET_NULL)
	event_name	= models.CharField(max_length=30)
	event_date	= models.DateField()
	artists 	= models.CharField(max_length=100, default='NO_ARTISTS')
	genre 		= models.CharField(max_length=100, default='NO_GENRE')
	upload		= models.FileField(upload_to = media_directory_path, null=True)  #the path where the image is uploaded to


