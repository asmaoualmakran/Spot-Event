from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SpotEventApp.serializers.address import Address as addressSerializer
from SpotEventApp.models.address import Address as addressModel


@api_view(['GET','POST'])
def address_request(request):
	if (request.method == 'GET'):
		addresses = addressModel.objects.all()
		serializer = addressSerializer(addresses, many=True)
		return Response(serializer.data)
	elif (request.method == 'POST'):
		serializer = addressSerializer(data=request.data)
		if (serializer.is_valid()):
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_address(request, address_id):
	try:
		address = addressModel.object.get(id=adress_id)
	except:
		return Response(serializer.errors, status=status.HTTP_400_NOT_FOUND)
	serializer = addressSerializer(data=request.data)
	if (serializer.is_valid()):
		address = serializer.save()
		serializer = addressSerializer(adress, context={'request':request})
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)