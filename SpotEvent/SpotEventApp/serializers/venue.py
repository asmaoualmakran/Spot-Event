from rest_framework import serializers
from SpotEventApp.models.venue import Venue as venueModel
from SpotEventApp.models.address import Address as addressModel


class Venue(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta: 
		model = venueModel
		fields = ('id', 'venue_name', 'address_id')
		extra_kwargs = {'address_id':{'view_name': 'api:address-detail'}}

class Create_venue(serializers.Serializer): #create own serializer to make sure the right key value pair are added to the right objects

	_venueFields = ('venue_name',)
	_addressFields = ('street','number','zip_code','city','country')

	venue_name 	= serializers.CharField(max_length=30)
	street 		= serializers.CharField(max_length=50)
	number 		= serializers.CharField(max_length=5)
	zip_code 	= serializers.CharField(max_length=10)
	city 		= serializers.CharField(max_length=20)
	country 	= serializers.CharField(max_length=20)

	def create(self, validated_data):
		data = {key:validated_data[key] for key in self._addressFields}
		address = addressModel.objects.create(**data)
		data = {key:validated_data[key] for key in self._venueFields}
		return venueModel.objects.create(**data,address_id=address)