# catalog serializer

from rest_framework import serializers
from catalog.models.Product import Product

class ProductSerializer(serializers.ModelSerializer):

  class Meta:
    model = Product
    fields = '__all__'

