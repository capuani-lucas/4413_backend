# authenticated route using rest framework

from rest_framework.views import APIView
from rest_framework.response import Response

from catalog.dao.catalog_dao import CatalogDAO
from catalog.serializers.catalog_serializer import CatalogSerializer

class CatalogView(APIView):

  serializer_class = CatalogSerializer

  def get(self, request):
    catalog_dao = CatalogDAO()
    catalog = catalog_dao.get_all_products()
    serializer = CatalogSerializer(catalog, many=True)

    return Response({
      'catalog': serializer.data
    })
  
class CatalogByCategoryView(APIView):

  serializer_class = CatalogSerializer

  def get(self, request, category_id):
    catalog_dao = CatalogDAO()
    catalog = catalog_dao.get_products_by_category(category_id)
    serializer = CatalogSerializer(catalog, many=True)

    return Response({
      'catalog': serializer.data
    })
  
class CatalogByIdView(APIView):

  serializer_class = CatalogSerializer

  def get(self, request, product_id):
    catalog_dao = CatalogDAO()
    catalog = catalog_dao.get_product_by_id(product_id)

    if not catalog:
      return Response({
        'catalog': None
      })

    serializer = CatalogSerializer(catalog)

    return Response({
      'catalog': serializer.data
    })