from rest_framework import serializers
from SpotEventApp.models.venue import Venue as venueModel

#class Venue(serializers.Serializer):
#	id = serializers.IntegerField(read_only = False)
#	venue_name = serializers.CharField(max_length = 30)
#	address_id = serializers.StringRelatedField(many=False)

#	def create(self, validated_data):
#		print('validated', validated_data)
#		return venueModel.Venue.objects.create(**validated_data)

#	def update(self, instance, validated_data):
#		instance = validated_data.get('venue_name', instance.venue_name)
#		instance.save()
#		return instance

class Venue(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta: 
		model = venueModel
		fields = ('id', 'venue_name')
		extra_kwargs = {'address':{'view_name': 'api:venue-detail'}}

class Create_venue(serializers.ModelSerializer):
	class Meta: 
		model = venueModel
		fields = ('venue_name','street','number','zip_code','country')