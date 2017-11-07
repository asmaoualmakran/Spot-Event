from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SpotEventApp.serializers.event import Event as eventSerializer
from SpotEventApp.models.event import Event as eventModel


@api_view(['GET','POST'])
def event_request(request):
	if (request.method == 'GET'):
		events = eventModel.objects.all()
		serializers = eventSerializer(events, many=True)
		return Response(serializers.data)
	elif (request.method == 'POST'):
		serializer = eventSerializer(data=request.data)
		if (serializer.is_valid()):
			serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

