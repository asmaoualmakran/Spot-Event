from rest_framework import serializers
from SpotEventApp.models import review as reviewModel


class Review(serializers.Serializer):
	id = serializers.IntergerField(read_only = True)
	# venue_id 
	score = serializers.IntergerField()
	review = serializers.TextField()

	def create(self, validated_data):
		print('validated', validated_data)
		return reviewModel.Review.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.score = serializers.get('score', instance.score)
		instance.review = serializers.get('review' instance.review)
		instance.save()
		return instance
