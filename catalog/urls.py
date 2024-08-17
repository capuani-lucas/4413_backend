from django.urls import path

from catalog.views.catalog_view import CatalogByCategoryView, CatalogByIdView, CatalogView

urlpatterns = [
  path('', CatalogView.as_view(), name='catalog'),
  # catalog by category
  path('category/<int:category_id>/', CatalogByCategoryView.as_view(), name='catalog_by_category'),
  # catalog by id
  path('<int:product_id>/', CatalogByIdView.as_view(), name='catalog_by_id'),
]
