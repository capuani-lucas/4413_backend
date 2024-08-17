# authenticated route using rest framework

from rest_framework.views import APIView
from rest_framework.response import Response

from catalog.dao.catalog_dao import CatalogDAO
from catalog.serializers.brand_serializer import BrandSerializer
from catalog.serializers.product_serializer import ProductSerializer
from catalog.serializers.category_serializer import CategorySerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CatalogView(APIView):

  serializer_class = ProductSerializer

  @swagger_auto_schema(
    operation_description="Retrieve all products in the catalog",
    manual_parameters=[
      openapi.Parameter('brand', openapi.IN_QUERY, description="Filter by brand", type=openapi.TYPE_STRING),
      openapi.Parameter('category', openapi.IN_QUERY, description="Filter by category", type=openapi.TYPE_INTEGER),
      openapi.Parameter('search', openapi.IN_QUERY, description="Search by name", type=openapi.TYPE_STRING),
      openapi.Parameter('sort_by', openapi.IN_QUERY, description="Sort by field", type=openapi.TYPE_STRING),
    ],
    responses={200: ProductSerializer(many=True)},
  )
  def get(self, request):

    brand = request.query_params.get('brand')
    category = request.query_params.get('category')
    search = request.query_params.get('search')
    sort_by = request.query_params.get('sort_by')


    catalog_dao = CatalogDAO()
    catalog = catalog_dao.get_all_products(
      brand=brand,
      category=category,
      search=search,
      sort_by=sort_by
    )
    serializer = ProductSerializer(catalog, many=True)

    return Response({
      'catalog': serializer.data
    })
  
class CatalogByCategoryView(APIView):

  serializer_class = ProductSerializer

  @swagger_auto_schema(
    operation_description="Retrieve products in the catalog by category",
    manual_parameters=[
      openapi.Parameter('category_id', openapi.IN_PATH, description="ID of the category", type=openapi.TYPE_INTEGER)
    ],
    responses={200: ProductSerializer(many=True)},
  )
  def get(self, request, category_id):
    catalog_dao = CatalogDAO()
    catalog = catalog_dao.get_products_by_category(category_id)
    serializer = ProductSerializer(catalog, many=True)

    return Response({
      'catalog': serializer.data
    })
  
class CatalogByIdView(APIView):

  serializer_class = ProductSerializer

  @swagger_auto_schema(
    operation_description="Retrieve a product by its ID",
    manual_parameters=[
      openapi.Parameter('product_id', openapi.IN_PATH, description="ID of the product", type=openapi.TYPE_INTEGER)
    ],
    responses={
      200: ProductSerializer(),
      404: openapi.Response('Product not found'),
    },
  )
  def get(self, request, product_id):
    catalog_dao = CatalogDAO()
    catalog = catalog_dao.get_product_by_id(product_id)

    if not catalog:
      return Response({
        'catalog': None
      })

    serializer = ProductSerializer(catalog)

    return Response({
      'catalog': serializer.data
    })
  
class CatalogGetCategoriesView(APIView):

  @swagger_auto_schema(
    operation_description="Retrieve all categories in the catalog",
    responses={200: CategorySerializer(many=True)},
  )
  def get(self, request):
    catalog_dao = CatalogDAO()
    categories = catalog_dao.get_categories()

    serializer = CategorySerializer(categories, many=True)
    return Response({
      'categories': serializer.data
    })
  
class CatalogGetBrandsView(APIView):

  @swagger_auto_schema(
    operation_description="Retrieve all brands in the catalog",
    responses={200: BrandSerializer(many=True)},
  )
  def get(self, request):
    catalog_dao = CatalogDAO()
    brands = catalog_dao.get_brands()

    serializer = BrandSerializer(brands, many=True)
    return Response({
      'brands': serializer.data
    })
