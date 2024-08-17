
from cart.models.Cart import Cart

class CartDAO():

  def get_cart_by_id(self, cart_id):
    return Cart.objects.filter(id=cart_id).first()

  def get_users_cart(self, user):
    return Cart.objects.filter(user=user)
  
  def add_to_cart(self, user, product, quantity):
    # Find or create cart item
    existing_cart = Cart.objects.filter(user=user, product=product).first()
    if existing_cart:
      existing_cart.quantity += 1
      existing_cart.save()
      return

    Cart.objects.create(
      user=user,
      product=product,
      quantity=quantity
    )

  def remove_from_cart(self, cart_id):

    cart_item = Cart.objects.filter(id=cart_id).first()
    if not cart_item:
      return

    cart_item.delete()
    return
  
  def update_cart_item(self, cart_id, quantity):
    cart_item = Cart.objects.filter(id=cart_id).first()
    if not cart_item:
      return

    cart_item.quantity = quantity
    cart_item.save()
    return

  def get_cart_by_product(self, user, product):
    return Cart.objects.filter(user=user, product=product).first()
  
  def clear_cart(self, user):
    Cart.objects.filter(user=user).delete()
    return