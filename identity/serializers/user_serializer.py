
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def validate_username(self, value):
    if not serializers.EmailField().run_validation(value):
        raise serializers.ValidationError("Enter a valid email address.")
    return value

  