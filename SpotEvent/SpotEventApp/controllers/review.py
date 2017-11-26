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
		serializer = reviewSerializer(data=request.data)
		if (serializer.is_valid()):
			serializer = Create_reviewSerializer(serializer.save(), context={'request':request})
			return Response(serializer.data)
		else: 
			return Response(serializer.errors)

@api_view(['GET'])
def single_review_request(request,pk):
	try:
		review = reviewModel.objects.get(id=pk)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)
	serializer = reviewSerializer(review, context={'request':request})
	return Response(serializer.data)