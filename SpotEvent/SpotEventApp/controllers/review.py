from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SpotEventApp.serializers.review import Review as reviewSerializer
from SpotEventApp.models.review import Review as reviewModel

@api_view(['GET','POST'])
def review_request(request):
	if (request.method == 'GET'):
		reviews = reviewModel.objects.all()
		serializers = reviewSerializer(reviews, many=True)
		return Response(serializers.data)
	elif (request.method == 'POST'):