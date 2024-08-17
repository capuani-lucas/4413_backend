

from catalog.models.Product import Product

class CatalogDAO():

  def get_all_products(self):
    products = Product.objects.filter(deleted_at=None)
    return products
  
  def get_product_by_id(self, product_id):
    product = Product.objects.filter(id=product_id).first()
    return product
  
  def get_products_by_category(self, category_id):
    products = Product.objects.filter(category=category_id, deleted_at=None)
    return products
