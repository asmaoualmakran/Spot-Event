from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SpotEventApp.serializers.address import Address as addressSerializer
from SpotEventApp.models.address import Address as addressModel


#@api_view(['GET'])
#def address_request(request):
#	if(request.method == 'GET'):
#		adresses = addressModel.object.all() #return all addresses
#		serializer = addressSerializer(many=True)
#		return Response(serializer.data)



