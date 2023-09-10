from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, categories, products, contact, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('add_product/', add_product, name='add_product'),
    path('contacts/', contact, name='contacts'),
    path('<int:pk>/products/', products, name='products'),
    # path('', home),
]
