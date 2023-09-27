from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ProductListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, contact, IndexView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/<int:pk>/', ProductListView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/edit/<int:pk>/', ProductDetailView.as_view(), name='product_edit'),
    path('contacts/', contact, name='contacts'),
]
