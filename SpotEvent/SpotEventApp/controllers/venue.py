from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SpotEventApp.serializers.venue import Venue as venueSerializer
from SpotEventApp.serializers.venue import Create_venue as Create_venueSerializer
from SpotEventApp.models.venue import Venue as venueModel
from SpotEventApp.serializers.address import Address as addressSerializer



@api_view(['GET','POST'])
def venue_request(request):
	if (request.method == 'GET'):
		venues = venueModel.objects.all()
		serializer = venueSerializer(venues, many=True, context={'request':request})
		return Response(serializer.data)

	elif (request.method =='POST'):
		serializer = Create_venueSerializer(data=request.data)
		if serializer.is_valid():
			serializer = venueSerializer(serializer.save(), context={'request':request})
			return Response(serializer.data)
		else: 
			return Response(serializer.errors)


@api_view(['GET'])
def single_venue_request(request, pk): 
	try: 
		venue = venueModel.objects.get(id=pk)
	except: 
		return Response(status=status.HTTP_404_NOT_FOUND)
	serializer = venueSerializer(venue, context={'request':request})
	return Response(serializer.data)