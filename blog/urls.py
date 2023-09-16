from django.urls import path

from blog.apps import BlogConfig
from blog.views import RecordCreateView, RecordListView, RecordDetailView, RecordUpdateView, RecordDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', RecordCreateView.as_view(), name='create'),
    path('', RecordListView.as_view(), name='list'),
    path('view/<int:pk>/', RecordDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', RecordUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', RecordDeleteView.as_view(), name='delete'),
    # path('categories/', CategoryListView.as_view(), name='categories'),
    # path('products/<int:pk>/', ProductListView.as_view(), name='products'),
    # path('products/create/', ProductCreateView.as_view(), name='product_create'),
    # path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    # path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    # path('contacts/', contact, name='contacts'),
]
