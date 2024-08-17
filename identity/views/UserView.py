from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from identity.serializers.UserSerializer import UserSerializer

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
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
