from rest_framework import serializers
from SpotEventApp.models import user as userModel


class User(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	first_name = serializers.CharField(max_length=30)
	last_name = serializers.CharField(max_length=30)
	birthday = serializers.DateField()
	email = serializers.EmailField()
	address_id = serializers.StringRelatedField(many=False)
#	address_id = serializers.HyperlinkedRelatedField(
#		many = False,
#		read_only = True,
#		view_name = 'user_address')


	def create(self, validated_data):
		print('validated', validated_data)
		return userModel.User.objects.create(**validated_data)
		# you're using the class the file is put in userModel

	def update(self, instance, validated_data):
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.birthday = validated_data.get('birthday', instance.birthday)
		instance.email = validated_data.get('email', instance.email)
		instance.save()
		return instance