from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SpotEventApp.serializers.user import User as userSerializer
from SpotEventApp.models.user import User as userModel
from SpotEventApp.serializers.address import Address as addressSerializer


@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('api:users', request=request, format=format)
		})

@api_view(['GET', 'POST'])
def user_request(request):
	if (request.method == 'GET' ):
		users = userModel.objects.all() # returns all users
		serializer = userSerializer(users, many=True) #many = True, -> list of multiple user 
		return Response(serializer.data)
	elif (request.method == 'POST'):
		serializer	= userSerializer(data=request.data)
		if (serializer.is_valid()):
			serializer.save()	
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_user_address(request, user_id):
	try:
		user = userModel.objects.get(id=user_id) 
	except:
		return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
	serializer = addressSerializer(data=request.data)
	if (serializer.is_valid()):
		address = serializer.save()
		user.address_id = address #set address id in the user model to the new address
		user.save()
		serializer = userSerializer(user, context={'request': request}) #only one user
		print ('user', user)
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)