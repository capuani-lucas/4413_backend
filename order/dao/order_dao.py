from order.models.Order import Order

class OrderDAO():

  def get_orders(self, user):
    orders = Order.objects.filter(user=user).order_by('-created_at')
    return orders
  
  def create_order(self, user, product, quantity, price, first_name, last_name, address):
    order = Order.objects.create(
      user=user,
      product=product,
      quantity=quantity,
      price=price,
      first_name=first_name,
      last_name=last_name,
      address=address
    )
    return order
