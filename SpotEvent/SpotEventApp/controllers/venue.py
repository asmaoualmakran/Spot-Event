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


@api_view(['GET','PUT','DELETE'])
def single_venue_request(request, pk): 
	try: 
		venue = venueModel.objects.get(id=pk)
	except venueModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if(request.method == 'GET'):	
		serializer = venueSerializer(venue, context={'request':request})
		return Response(serializer.data, status=status.HTTP_200_OK)

	elif(request.method == 'PUT'):
		serializer = venueSerializer(venue, data=request.data, context={'request':request})
		if(serializer.is_valid()):
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		venue.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)	