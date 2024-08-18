from order.models.Order import Order

class OrderDAO():

  def get_orders(self, user):
    orders = Order.objects.filter(user=user).order_by('-created_at')
    return orders
  
  def create_order(self, user, product, quantity, price, first_name, last_name, address, card_number, card_expiry, card_cvv):
    order = Order.objects.create(
      user=user,
      product=product,
      quantity=quantity,
      price=price,
      first_name=first_name,
      last_name=last_name,
      address=address,
      card_number=card_number,
      card_expiry=card_expiry,
      card_cvv=card_cvv
    )
    return order
