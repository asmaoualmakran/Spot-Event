from rest_framework import serializers
from SpotEventApp.models.event import Event as eventModel

class Event(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta: 
		model = eventModel
		fields = ('id','venue_id', 'event_name', 'artists')
		extra_kwargs = {'venue':{'view_name': 'api:venue-detail'}}

class CreateEvent(serializers.ModelSerializer):
	class Meta: 
		model = eventModel
		fields = ('venue_id', 'event_name', 'artists')



