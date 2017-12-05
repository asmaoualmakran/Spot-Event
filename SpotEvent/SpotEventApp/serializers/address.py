from rest_framework import serializers
from SpotEventApp.models.address import Address as addressModel



class Address(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = addressModel
		fields = ('id','street','number','zip_code','city','country')
	

class Create_address(serializers.ModelSerializer):

	 class Meta: 
	 	model = addressModel
	 	fields = ('street','number','zip_code','city','country')

