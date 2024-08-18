from rest_framework.views import APIView
from rest_framework.response import Response

from cart.dao.cart_dao import CartDAO
from catalog.dao.catalog_dao import CatalogDAO
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from order.dao.order_dao import OrderDAO
from order.serializers.order_serializer import OrderSerializer

class OrderView(APIView):

  serializer_class = OrderSerializer

  @swagger_auto_schema(
    operation_description="Retrieve all orders",
    responses={200: OrderSerializer(many=True)},
  )
  def get(self, request):
    user = request.user
    order_dao = OrderDAO()
    orders = order_dao.get_orders(user)
    serializer = OrderSerializer(orders, many=True)
    return Response({
      'orders': serializer.data
    })
  
  @swagger_auto_schema(
    request_body=openapi.Schema(type=openapi.TYPE_OBJECT,
      required=['first_name', 'last_name', 'address'],
      properties={
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First name of the user'),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last name of the user'),
        'address': openapi.Schema(type=openapi.TYPE_STRING, description='Address of the user'),
        'card_number': openapi.Schema(type=openapi.TYPE_STRING, description='16 Digit card number'),
        'card_expiry': openapi.Schema(type=openapi.TYPE_STRING, description='Card expiry MMYY'),
        'card_cvv': openapi.Schema(type=openapi.TYPE_STRING, description='3 Digit CVV number'),
      }
    ),
    responses={
      201: openapi.Response('Created'),
      400: openapi.Response('Bad Request: Cart is empty'),
    }
  )
  def post(self, request):
    user = request.user

    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    address = request.data.get('address')
    card_number = request.data.get('card_number')
    card_expiry = request.data.get('card_expiry')
    card_cvv = request.data.get('card_cvv')

    serializer = OrderSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    cart_dao = CartDAO()
    cart_items = cart_dao.get_users_cart(user)
    if not cart_items:
      return Response({
        'error': 'Cart is empty'
      }, status=400)
    
    order_dao = OrderDAO()
    product_dao = CatalogDAO()
    for cart_item in cart_items:
      order_dao.create_order(
        user=user,
        product=cart_item.product,
        quantity=cart_item.quantity,
        price=cart_item.product.price,
        first_name=first_name,
        last_name=last_name,
        address=address,
        card_number=card_number,
        card_expiry=card_expiry,
        card_cvv=card_cvv
      )
      product_dao.decrease_stock(cart_item.product, cart_item.quantity)
      cart_dao.remove_from_cart(cart_item.id)
    
    return Response(status=201)
