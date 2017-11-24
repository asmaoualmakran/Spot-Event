from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SpotEventApp.serializers.event import Event as eventSerializer
from SpotEventApp.serializers.event import Create_event as Create_eventSerializer
from SpotEventApp.models.event import Event as eventModel
from SpotEventApp.serializers.venue import Venue as venueSerializer


		


@api_view(['GET','POST'])
def event_request(request):
	if (request.method == 'GET'):
		events = eventModel.objects.all()
		serializers = eventSerializer(events, many=True, context={'request': request})
		return Response(serializers.data)
	elif (request.method == 'POST'):
		serializer = eventSerializer(data=request.data)
		if (serializer.is_valid()):
			serializer = Create_eventSerializer(serializer.save(), context={'request': request})
			return Response(serializer.data)
		else:
			return Response(serializer.errors)

