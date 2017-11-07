from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SpotEventApp.serializers.venue import Venue as venueSerializer
from SpotEventApp.models.venue import Venue as venueModel
from SpotEventApp.serializers.address import Address as addressSerializer

@api_view(['GET','POST'])
def venue_request(request): 
	if (request.method == 'GET'):
		venues = venueModel.objects.all()
		serializer = venueSerializer(venues, many=True)
		return Response(serializer.data)
	elif (request.method == 'POST'):
		serializer = venueSerializer(data=request.data)
		if (serializer.is_valid()):
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_venue_address(request,venue_id):
	try: 
		venue = venueModel.objects.get(id=venue_id)
	except:
		return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)
	serializer = addressSerializer(data=request.data)
	if (serializer.is_valid()):
		address = serializer.save()
		venue.address_id = address
		venue.save()
		serializer = venueSerializer(venue, context={'request':request})
		print ('venue', venue)
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)