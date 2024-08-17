from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from identity.dao.identity_dao import IdentityDAO
from identity.serializers.user_serializer import UserSerializer

class CreateUserView(generics.CreateAPIView):
  serializer_class = UserSerializer
  authentication_classes = []
  permission_classes = []

  def create(self, request, *args, **kwargs):

    if 'username' not in request.data:
      return Response({'error': 'username is required'}, status=status.HTTP_400_BAD_REQUEST)
    if 'password' not in request.data:
      return Response({'error': 'password is required'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    identity_dao = IdentityDAO()
    user = identity_dao.create_user(username=serializer.validated_data['username'], password=serializer.validated_data['password'])

    serialized_user = UserSerializer(user)
    return Response(serialized_user.data, status=status.HTTP_201_CREATED)

    
    
