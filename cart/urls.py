from django.urls import path

from cart.views.cart_view import CartView, ClearCartView

urlpatterns = [
  path('', CartView.as_view(), name='cart'),
  path('add/<int:product_id>/', CartView.as_view(), name='cart_add'),
  path('update/<int:cart_id>/', CartView.as_view(), name='cart_update'),
  path('remove/<int:cart_id>/', CartView.as_view(), name='cart_remove'),
  path('clear/', ClearCartView.as_view(), name='cart_clear'),
]
