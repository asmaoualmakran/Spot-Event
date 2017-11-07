from rest_framework import serializers
from SpotEventApp.models import venue as venueModel

class Venue(serializers.Serializer):
	id = serializers.IntegerField(read_only = True)
	venue_name = serializers.CharField(max_length = 30)
	address_id = serializers.StringRelatedField(many=False)

	def create(self, validated_data):
		print('validated', validated_data)
		return venueModel.Venue.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance = validated_data.get('venue_name', instance.venue_name)
		instance.save()
		return instance