# Category django model

from django.db import models

class Category(models.Model):
  
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  description = models.TextField()
  deleted_at = models.DateTimeField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
  
  # create history on save
  def save(self, *args, **kwargs):
    super(Category, self).save(*args, **kwargs)
    category_history = CategoryHistory(
      category=self,
      name=self.name,
      description=self.description
    )
    category_history.save()
  
class CategoryHistory(models.Model):
  
  id = models.AutoField(primary_key=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.TextField()
  deleted_at = models.DateTimeField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name