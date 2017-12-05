from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SpotEventApp.serializers.event import Event as eventSerializer
from SpotEventApp.serializers.event import Create_event as Create_eventSerializer
from SpotEventApp.models.event import Event as eventModel
from SpotEventApp.serializers.venue import Venue as venueSerializer 
#venueSerializer is momenteel nog niet nodig er moet pas een venue gemaakt 
#worden wanneer de venue nog niet zou bestaan
#TODO: handel nog niet bestaande venues af



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


@api_view(['GET','PUT','DELETE'])
def single_event_request(request,pk):
	try: 
		event = eventModel.objects.get(id=pk)
	except eventModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if(request.method == 'GET'):
		serializer = eventSerializer(event, context={'request':request})
		return Response(serializer.data, status=status.HTTP_200_OK)

	elif(request.method == 'PUT'):
		serializer = eventSerializer(event, data=request.data, context={'request':request})
		if(serializer.is_valid()):
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		event.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
