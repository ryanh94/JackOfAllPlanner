from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import User
from .serializers import UserSerializer

@api_view(['GET'])
def getUser(request, id):
    user = User.objects.filter(id=id)
    serialized_users = UserSerializer(user, many=True)

    if len(serialized_users.data) > 0:
        return Response(serialized_users.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def createUser(request):
    serialize_user = UserSerializer(data=request.data)
    
    if serialize_user.is_valid():
        serialize_user.save()
  
        return Response(serialize_user.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


