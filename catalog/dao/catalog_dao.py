

from catalog.models.Brand import Brand
from catalog.models.Product import Product
from catalog.models.Category import Category

class CatalogDAO():

  def get_all_products(self, brand, category, search, sort_by):
    products = Product.objects.filter()

    if brand:
      products = products.filter(brand=brand)
    
    if category:
      products = products.filter(category=category)

    if search:
      products = products.filter(name__icontains=search)
    
    if sort_by:
      products = products.order_by(sort_by)

    return products
  
  def get_product_by_id(self, product_id):
    product = Product.objects.filter(id=product_id).first()
    return product
  
  def get_products_by_category(self, category_id):
    products = Product.objects.filter(category=category_id)
    return products
  
  def get_categories(self):
    categories = Category.objects.filter()
    return categories

  def get_brands(self):
    brands = Brand.objects.filter()
    return brands
