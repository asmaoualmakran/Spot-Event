from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SpotEventApp.serializers.review import Review as reviewSerializer
from SpotEventApp.serializers.review import Create_review as Create_reviewSerializer
from SpotEventApp.models.review import Review as reviewModel

@api_view(['GET','POST'])
def review_request(request):
	if (request.method == 'GET'):
		reviews = reviewModel.objects.all()
		serializers = reviewSerializer(reviews, many=True, context={'request':request})
		return Response(serializers.data)
	elif (request.method == 'POST'):
		serializer = Create_reviewSerializer(data=request.data)
		if (serializer.is_valid()):
			serializer = serializers.reviewSerializer(serializer.save(), context={'request':request})
			return Response(serializer.data)
		else: 
			return Response(serializer.errors)