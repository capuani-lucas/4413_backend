from rest_framework.views import exception_handler
from rest_framework import serializers

def custom_exception_handler(exc, context):
  response = exception_handler(exc, context)

  if response is not None:
    print(response.data)
    if isinstance(exc, (serializers.ValidationError,)):
      response.data = {'error': list(response.data.values())[0][0]}
    else:
      response.data = {'error': response.data}

  return response
