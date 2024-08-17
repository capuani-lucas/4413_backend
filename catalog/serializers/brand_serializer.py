# catalog serializer

from rest_framework import serializers
from catalog.models.Brand import Brand

class BrandSerializer(serializers.ModelSerializer):

  class Meta:
    model = Brand
    fields = '__all__'
