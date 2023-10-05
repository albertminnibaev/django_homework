from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ProductListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, contact, IndexView, ProductDetailView, VersionListView, VersionCreateView, VersionUpdateView, \
    VersionDeleteView, VersionDetailView

app_name = CatalogConfig.name


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/<int:pk>/', ProductListView.as_view(), name='products'),
    path('products/create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('products/update/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/edit/<int:pk>/', ProductDetailView.as_view(), name='product_edit'),
    path('version/<int:pk>/', VersionListView.as_view(), name='version'),
    path('version/create/', never_cache(VersionCreateView.as_view()), name='version_create'),
    path('version/update/<int:pk>/', never_cache(VersionUpdateView.as_view()), name='version_update'),
    path('version/delete/<int:pk>/', VersionDeleteView.as_view(), name='version_delete'),
    path('version/edit/<int:pk>/', VersionDetailView.as_view(), name='version_edit'),
    path('contacts/', contact, name='contacts'),
]
