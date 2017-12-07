from rest_framework import serializers
from SpotEventApp.models.user import User as userModel
from SpotEventApp.models.address import Address as addressModel


class User(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta: 
		model = userModel
		fields = ('id','username','first_name','last_name', 'birthday', 'email', 'address_id')			 
		extra_kwargs = {'address_id': {'view_name': 'api:address-detail'}}


class Create_user(serializers.Serializer):
	_userFields = ('username','first_name','last_name','birthday', 'email')
	_addressFields = ('street','number', 'zip_code', 'city', 'country')

	username 	= serializers.CharField(max_length=30)
	first_name 	= serializers.CharField(max_length=30)
	last_name 	= serializers.CharField(max_length=30)
	birthday 	= serializers.DateField()
	email 		= serializers.EmailField()
	street 		= serializers.CharField(max_length=50)
	number 		= serializers.CharField(max_length=5)
	zip_code 	= serializers.CharField(max_length=10)
	city 		= serializers.CharField(max_length=20)
	country 	= serializers.CharField(max_length=20)

	def create(self, validated_data):
		data = {key:validated_data[key] for key in self._addressFields}
		address = addressModel.objects.create(**data)
		data = {key:validated_data[key] for key in self._userFields}
		print(data)
		return userModel.objects.create(**data,address_id=address)




