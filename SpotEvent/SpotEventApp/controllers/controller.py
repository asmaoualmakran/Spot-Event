# Entry point for the api 

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'user': reverse('api:user', request=request, format=format),
        'address': reverse('api:address', request=request, format=format),
        'venue': reverse('api:venue', request=request, format=format),
        'event': reverse('api:event', request=request, format=format),
        'review': reverse('api:review', request=request, format=format),
    })