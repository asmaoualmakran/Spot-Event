from rest_framework import serializers
from SpotEventApp.models.review import Review as reviewModel


#class Review(serializers.Serializer):
#	id = serializers.IntergerField(read_only = True)
#	# venue_id 
#	score = serializers.IntergerField()
#	review = serializers.TextField()

#	def create(self, validated_data):
#		print('validated', validated_data)
#		return reviewModel.Review.objects.create(**validated_data)

#	def update(self, instance, validated_data):
#		instance.score = serializers.get('score', instance.score)
#		instance.review = serializers.get('review' instance.review)
#		instance.save()
#		return instance

class Review(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta: 
		model = reviewModel
		fields = ('id', 'venue_id', 'score','review')
		extra_kwargs = {'user':{'view_name': 'api:user_detail'}}

class Create_review(serializers.ModelSerializer):
	class Meta: 
		model = reviewModel
		field = {'user_id', 'venue_id', 'score','review'}