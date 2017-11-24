from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SpotEventApp.serializers.user import User as userSerializer
from SpotEventApp.serializers.user import Create_user as Create_userSerializer
from SpotEventApp.models.user import User as userModel
from SpotEventApp.serializers.address import Address as addressSerializer
#identifier serializer doesn't have to imported, inheritance form that class
#address is a foreign key of identifier, thus also for user

#this wil get all users and retrun it or add a user to 
#the existing list of users 
# when posting an addres needs to be created too
@api_view(['GET', 'POST'])
def user_request(request):
	if (request.method == 'GET' ):
		users = userModel.objects.all() # returns all users
		serializer = userSerializer(users, many=True, context={'request':request}) #many = True, -> list of multiple user 
		return Response(serializer.data)
	elif (request.method == 'POST'):
		serializer	= Create_userSerializer(data=request.data) # hier creeeren 
		if (serializer.is_valid()):
			user = serializer.save()
			print('created')
			serializer = userSerializer(user, context={'request':request} )	# de gecreeerde user terug geven
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#when creating a user, an address has to be created 
# --> adding a new value to identifier
#post request has to be adjusted

#@api_view(['POST'])
#def create_user_address(request, user_id):
#	try:
#		user = userModel.objects.get(id=user_id) 
#	except:
#		return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#	serializer = addressSerializer(data=request.data)
#	if (serializer.is_valid()):
#		address = serializer.save()
#		user.address_id = address #set address id in the user model to the new address
#		user.save()
#		serializer = userSerializer(user, context={'request': request}) #only one user
#		print ('user', user)
#		return Response(serializer.data, status=status.HTTP_201_CREATED)
#	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#this will get one user or modify / detete one user, using the primary key of the entity

#@api_view(['GET','PUST','DELETE'])
#def user(request, pk):
#	try:
#		user = userModel.objects.get(id=pk)  #check if the instance exist
#	except userModel.DoesNotExist:
#		return Response(status=status.HTTP_404_NOT_FOUND)

#	if (request.method == 'GET'):
#		serializer = userModel(user)
#		return Response(serializer.data, status=status.HTTP_200_OK)

#	elif (request.method == 'PUST'):

#	elif (request.method == 'DELETE'):
