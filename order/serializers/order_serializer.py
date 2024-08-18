# Order serializer

from datetime import datetime
from rest_framework import serializers
from order.models.Order import Order
from catalog.serializers.product_serializer import ProductSerializer
from identity.serializers.user_serializer import UserSerializer

class OrderSerializer(serializers.ModelSerializer):
  product = ProductSerializer(required=False)
  class Meta:
    model = Order
    exclude = ['user']

    extra_kwargs = {
      'quantity': {'required': False},
      'price': {'required': False},
    }

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
  
  def validate_card_number(self, value):
    if not value or len(value) != 16:
      raise serializers.ValidationError("16 Digit Card number is required")
    
    if not value.isdigit():
      raise serializers.ValidationError("Card number should be numeric")

    return value
  
  def validate_card_expiry(self, value):
    if not value or len(value) != 4:
      raise serializers.ValidationError("Card expiry is required. 3 or 4 digits MMYY")

    if not value.isdigit():
      raise serializers.ValidationError("Card expiry should be numeric")
    
    if int(value[:2]) > 12:
      raise serializers.ValidationError("Card expiry month should be less than 12")
    
    if int(value[2:]) < int(str(datetime.now().year)[2:]):
      raise serializers.ValidationError("Card expiry year cant be in the past")
    
    # check if expired
    if int(value[2:]) == int(str(datetime.now().year)[2:]) and int(value[:2]) < datetime.now().month:
      raise serializers.ValidationError("Card has expired")

    
    return value
  
  def validate_card_cvv(self, value):
    if not value or len(value) != 3:
      raise serializers.ValidationError("Card CVV is required and should be 3 digits")
    
    if not value.isdigit():
      raise serializers.ValidationError("Card CVV should be numeric")

    return value
