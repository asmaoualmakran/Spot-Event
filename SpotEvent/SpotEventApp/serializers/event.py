from rest_framework import serializers
from SpotEventApp.models import event as eventModel

class Event(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)

	venue_id = serializers.StringRelatedField(many=False)
	#venue_id = serializers.PrimaryKeyRelatedField(
	#	many = True,
	#	read_only =False,
	#	view_name = 'venue_detail')
	
	event_name = serializers.CharField(max_length=20)
	artists = serializers.CharField(max_length=100, default='NO_ARTISTS')


	def create( self, validated_data):
		print('validated', validated_data)
		return eventModel.Event.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.venue_id = validated_data.get('venue_id', instance.venue_id)
		instance.event_name = validated_data.get('event_name'. instance.event)
		instance.save()
		return instance


