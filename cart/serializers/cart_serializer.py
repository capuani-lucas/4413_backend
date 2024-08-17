# Cart model serializer

from rest_framework import serializers
from cart.models.Cart import Cart
from catalog.serializers.product_serializer import ProductSerializer
from django.contrib.auth.models import User

from identity.serializers.user_serializer import UserSerializer

class CartSerializer(serializers.ModelSerializer):
  
  cart_quantity = serializers.IntegerField(write_only=True)

  class Meta:
    model = Cart
    # include all fields except user
    exclude = ['user']

  def validate_quantity(self, value):
    if value < 1 or value > 99:
      raise serializers.ValidationError('Quantity must be greater than 0 and less than 100')
    return value
  
  def validate(self, data):
    
    product = data.get('product')
    quantity = data.get('quantity')
    cart_quantity = data.get('cart_quantity')

    if quantity + cart_quantity > product.stock:
      raise serializers.ValidationError('Quantity exceeds stock')
    
    return data


