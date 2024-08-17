# Order django model

from django.db import models
from django.contrib.auth.models import User
from catalog.models.Product import Product

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  price = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  address = models.CharField(max_length=200)

  def __str__(self):
    return self.product.name

  def create_history(self):
    order_history = OrderHistory(
      order=self,
      user=self.user,
      product=self.product,
      quantity=self.quantity,
      price=self.price,
      address=self.address,
      first_name=self.first_name,
      last_name=self.last_name
    )
    order_history.save()
  
  def save(self, *args, **kwargs):
    super(Order, self).save(*args, **kwargs)
    self.create_history()

  def create(self, *args, **kwargs):
    self.create_history()
    super(Order, self).create(*args, **kwargs)


class OrderHistory(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  price = models.FloatField()

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)

  address = models.CharField(max_length=200)

  def __str__(self):
    return self.product.name
