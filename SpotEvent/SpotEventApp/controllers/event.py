from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from SpotEventApp.serializers.event import Event as eventSerializer
from SpotEventApp.serializers.event import CreateEvent as CreateEventSerializer
from SpotEventApp.models.event import Event as eventModel
from SpotEventApp.serializers.venue import Venue as venueSerializer

@api_view(['GET'])
def event_root(request, format=None):
	return Response({
		'events': reverse('api:events', request=request, format=format)
		})


@api_view(['GET','POST'])
def event_request(request):
	if (request.method == 'GET'):
		events = eventModel.objects.all()
		serializers = eventSerializer(events, many=True, context={'request': request})
		return Response(serializers.data)
	elif (request.method == 'POST'):
		serializer = eventSerializer(data=request.data)
		if (serializer.is_valid()):
			serializer = CreateEventSerializer(serializer.save(), context={'request': request})
			return Response(serializer.data)
		else:
			return Response(serializer.errors)

