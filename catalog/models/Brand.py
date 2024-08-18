# Brand django model

from django.db import models

class Brand(models.Model):
  
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  image_url = models.CharField(max_length=2000)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

  def create_history(self):
    brand_history = BrandHistory(
      brand=self,
      name=self.name,
      image_url=self.image_url
    )
    brand_history.save()

  def save(self, *args, **kwargs):
    super(Brand, self).save(*args, **kwargs)
    self.create_history()

  def create(self, *args, **kwargs):
    self.create_history()
    super(Brand, self).create(*args, **kwargs)

class BrandHistory(models.Model):
  
  id = models.AutoField(primary_key=True)
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  image_url = models.CharField(max_length=2000)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
