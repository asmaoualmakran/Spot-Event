from rest_framework import serializers
from SpotEventApp.models.event import Event as eventModel

class Event(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta: 
		model = eventModel
		fields = ('id','venue_id','user_id','event_name','event_date','artists','genre', 'upload')
		extra_kwargs = {'venue_id':{'view_name': 'api:venue-detail'},'user_id':{'view_name': 'api:user-detail'}}

class Create_event(serializers.ModelSerializer):
	
	class Meta: 
		model = eventModel
		fields = ('venue_id','user_id','event_name','event_date','artists','genre', 'upload')





