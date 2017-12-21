from rest_framework import serializers
from SpotEventApp.models.review import Review as reviewModel


class Review(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta: 
		model = reviewModel
		fields = ('id','user_id','venue_id', 'score','review')
		extra_kwargs = {'user_id':{'view_name': 'api:user-detail'},'venue_id':{'view_name': 'api:venue-detail'}}


class Create_review(serializers.ModelSerializer):

	class Meta: 
		model = reviewModel
		fields = ('user_id', 'venue_id', 'score','review')
	