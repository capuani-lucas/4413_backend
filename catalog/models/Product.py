# product django model

from django.db import models

class Product(models.Model):

  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  stock = models.IntegerField()
  image_url = models.CharField(max_length=2000)
  deleted_at = models.DateTimeField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  category = models.ForeignKey('Category', on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  # create history on save
  def save(self, *args, **kwargs):
    super(Product, self).save(*args, **kwargs)
    product_history = ProductHistory(
      product=self,
      name=self.name,
      description=self.description,
      price=self.price,
      stock=self.stock,
      image_url=self.image_url
    )
    product_history.save()

class ProductHistory(models.Model):

  id = models.AutoField(primary_key=True)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  stock = models.IntegerField()
  image_url = models.CharField(max_length=2000)
  deleted_at = models.DateTimeField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
