# catalog serializer

from rest_framework import serializers
from catalog.models.Product import Product
from catalog.serializers.brand_serializer import BrandSerializer
from catalog.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):

  category = CategorySerializer(read_only=True)
  brand = BrandSerializer(read_only=True)

  class Meta:
    model = Product
    fields = '__all__'

