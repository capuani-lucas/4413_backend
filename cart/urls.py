from django.urls import path

from cart.views.cart_view import (
  CartGetView, CartAddView, CartRemoveView, CartUpdateView, ClearCartView
)

urlpatterns = [
  path('', CartGetView.as_view(), name='cart'),
  path('add/<int:product_id>/', CartAddView.as_view(), name='cart_add'),
  path('update/<int:cart_id>/', CartUpdateView.as_view(), name='cart_update'),
  path('remove/<int:cart_id>/', CartRemoveView.as_view(), name='cart_remove'),
  path('clear/', ClearCartView.as_view(), name='cart_clear'),
]
