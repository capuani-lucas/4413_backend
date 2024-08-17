from rest_framework.views import APIView
from rest_framework.response import Response

from cart.dao.cart_dao import CartDAO
from cart.serializers.cart_serializer import CartSerializer
from catalog.dao.catalog_dao import CatalogDAO
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CartGetView(APIView):

  serializer_class = CartSerializer

  @swagger_auto_schema(
    operation_description="Retrieve the user's cart",
    responses={200: CartSerializer(many=True)},
  )
  def get(self, request):
    cart_dao = CartDAO()
    cart = cart_dao.get_users_cart(request.user)
    serializer = CartSerializer(cart, many=True)

    return Response({
      'cart': serializer.data
    })
  
class CartRemoveView(APIView):

  @swagger_auto_schema(
    responses={
      204: openapi.Response('No Content'),
      404: openapi.Response('Not Found: Cart item not found or does not belong to the user'),
    }
  )
  def delete(self, request, cart_id):
    cart_dao = CartDAO()

    cart = cart_dao.get_cart_by_id(cart_id)
    if not cart or cart.user.id != request.user.id:
      return Response({
        'error': 'Cart item not found'
      }, status=404)

    cart_dao.remove_from_cart(cart_id)
    return Response(status=204)

class CartUpdateView(APIView):
  @swagger_auto_schema(
    request_body=openapi.Schema(type=openapi.TYPE_OBJECT,
      required=['quantity'],
      properties={
        'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description='Quantity of the product'),
      }
    ),
    responses={
      204: openapi.Response('No Content'),
      400: openapi.Response('Bad Request: Quantity required or validation error'),
      404: openapi.Response('Not Found: Cart item not found or does not belong to the user'),
    }
  )
  def put(self, request, cart_id):
    cart_dao = CartDAO()

    cart = cart_dao.get_cart_by_id(cart_id)
    if not cart or cart.user.id != request.user.id:
      return Response({
        'error': 'Cart item not found'
      }, status=404)

    quantity = request.data.get('quantity')
    if not quantity:
      return Response({
        'error': 'Quantity required'
      }, status=400)
    
    quantity = request.data.get('quantity', 1)
    data = {
      'product_stock': cart.product.stock,
      'quantity': quantity,
      'cart_quantity': 0
    }
    # check quantity valid in serializer
    serializer = CartSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    cart_dao.update_cart_item(cart_id, quantity)

    return Response(status=204)

class CartAddView(APIView):
  # also takes in quantity in the request body
  @swagger_auto_schema(
    request_body=openapi.Schema(type=openapi.TYPE_OBJECT,
      required=['quantity'],
      properties={
        'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description='Quantity of the product'),
      }
    ),
    responses={
      201: openapi.Response('Created'),
      400: openapi.Response('Bad Request: Product not found or validation error'),
    }
  )
  def post(self, request, product_id):
    cart_dao = CartDAO()
    catalog_dao = CatalogDAO()

    product = catalog_dao.get_product_by_id(product_id)
    if not product:
      return Response({
        'error': 'Product not found'
      }, status=400)

    cart = cart_dao.get_cart_by_product(request.user, product)
    
    quantity = request.data.get('quantity', 1)
    data = {
      'product_stock': product.stock,
      'cart_quantity': cart.quantity if cart else 0,
      'quantity': quantity
    }
    # check quantity valid in serializer
    serializer = CartSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    cart_dao.add_to_cart(request.user, product, quantity)

    # Return only status
    return Response(status=201)


class ClearCartView(APIView):
  @swagger_auto_schema(
    responses={204: openapi.Response('No Content')}
  )
  def post(self, request):
    cart_dao = CartDAO()
    cart_dao.clear_cart(request.user)

    return Response(status=204)
