from rest_framework import serializers
from SpotEventApp.models.user import User as userModel
from SpotEventApp.models.address import Address as addressModel


#class User(serializers.Serializer):
#	id = serializers.IntegerField(read_only=True)
#	first_name = serializers.CharField(max_length=30)
#	last_name = serializers.CharField(max_length=30)
#	birthday = serializers.DateField()
#	email = serializers.EmailField()
#	address_id = serializers.StringRelatedField(many=False)
##	address_id = serializers.HyperlinkedRelatedField(
##		many = False,
##		read_only = True,
##		view_name = 'user_address')
#

#	def create(self, validated_data):
#		print('validated', validated_data)
#		return userModel.User.objects.create(**validated_data)
#		# you're using the class the file is put in userModel

#	def update(self, instance, validated_data):
#		instance.first_name = validated_data.get('first_name', instance.first_name)
#		instance.last_name = validated_data.get('last_name', instance.last_name)
#		instance.birthday = validated_data.get('birthday', instance.birthday)
#		instance.email = validated_data.get('email', instance.email)
#		instance.save()
#		return instance


class User(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta: 
		model = userModel
		fields = ('id','first_name','last_name', 'birthday', 'email', 'address_id')			 
		extra_kwargs = {'address_id': {'view_name': 'api:address-detail'}}


class Create_user(serializers.Serializer):
	_userFields = ('first_name','last_name','birthday', 'email')
	_addressFields = ('street','number', 'zip_code', 'country')

	first_name = serializers.CharField(max_length = 30)
	last_name = serializers.CharField(max_length = 30)
	birthday = serializers.DateField()
	email = serializers.EmailField()
	street = serializers.CharField(max_length = 50)
	number = serializers.CharField(max_length = 5)
	zip_code = serializers.CharField(max_length = 10)
	country = serializers.CharField(max_length = 20)

	def create(self, validated_data):
		data = {key:validated_data[key] for key in self._addressFields}
		address = addressModel.objects.create(**data)
		data = {key:validated_data[key] for key in self._userFields}
		print(data)
		return userModel.objects.create(**data,address_id=address)


	# class Meta: 
	# 	model = userModel
	# 	fields = ('first_name','last_name','birthday', 
	# 			  'email','street', 'number', 'zip_code', 'country')

