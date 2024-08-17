# Order serializer

from rest_framework import serializers
from order.models.Order import Order
from catalog.serializers.product_serializer import ProductSerializer
from identity.serializers.user_serializer import UserSerializer

class OrderSerializer(serializers.ModelSerializer):
  product = ProductSerializer()
  class Meta:
    model = Order
    exclude = ['user']

  def validate_first_name(self, value):
    if not value:
      raise serializers.ValidationError("First name is required")
    return value
  
  def validate_last_name(self, value):
    if not value:
      raise serializers.ValidationError("Last name is required")
    return value
  
  def validate_address(self, value):
    if not value:
      raise serializers.ValidationError("Address is required")
    return value
