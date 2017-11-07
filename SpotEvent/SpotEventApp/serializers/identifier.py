from rest_framework import serializers
from SpotEventApp.models import identifier as identifierModel

class Identifier(serializers.Serializer):
	id = serializers.IntergerField(read_only = True)
#	address_id = serializers.IntergerField()

	def create(self, validated_data):
		print('validated', validated_data)
		return identifierModel.Identifier.objects.create(**validated_data)

	def update(self, instance, validated_data):

		## write code here
		instance.save()
		return instance
