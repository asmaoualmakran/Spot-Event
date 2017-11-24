from rest_framework import serializers
from SpotEventApp.models import address as addressModel


#class Address(serializers.Serializer):
#	id = serializers.IntegerField(read_only = True)
#	street = serializers.CharField(max_length = 50)
#	number = serializers.CharField(max_length = 5)
#	zip_code = serializers.CharField(max_length = 10)
#	country = serializers.CharField(max_length = 20)

#	def create(self, validate_data):
#		print('validated', validate_data)
#		return addressModel.Address.objects.create(**validate_data)

#	def update(self, instance, validate_data):
#		instance.street = validate_data.get('street', instance.street)
#		instance.number = validate_data.get('number', instance.number)
#		instance.zip_code = validate_data.get('zip_code', instance.zip_code)
#		instance.country = validate_data.get('country',instance.country)
#		instance.save()
#		return instance


class Address(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)


	class Meta:
		model = addressModel
		fields = ('id','street','number','zip_code','city','country')
	

class createAddress(serializers.ModelSerializer):

	 class Meta: 
	 	model = addressModel
	 	field = ('street','number','zip_code','city','country')
