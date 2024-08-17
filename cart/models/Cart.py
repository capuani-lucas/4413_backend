# Cart django model

from django.db import models
from django.contrib.auth.models import User
from catalog.models.Product import Product

class Cart(models.Model):

  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField()

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def create_history(self):
    cart_history = CartHistory(
      cart=self,
      user=self.user,
      product=self.product,
      quantity=self.quantity
    )
    cart_history.save()

  def save(self, *args, **kwargs):
    super(Cart, self).save(*args, **kwargs)
    self.create_history()
  
  def create(self, *args, **kwargs):
    self.create_history()
    super(Cart, self).create(*args, **kwargs)

  def __str__(self):
    return self.product.name
  
class CartHistory(models.Model):
  
  id = models.AutoField(primary_key=True)
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.product.name
