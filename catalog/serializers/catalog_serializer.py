# catalog serializer

from rest_framework import serializers
from catalog.models import Product

class CatalogSerializer(serializers.ModelSerializer):

  model = Product
  fields = '__all__'

