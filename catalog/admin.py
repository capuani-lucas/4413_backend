from django.contrib import admin

# Register your models here.

from catalog.models.Product import Product
from catalog.models.Category import Category

admin.site.register(Product)
admin.site.register(Category)