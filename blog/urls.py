from django.urls import path
from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from blog.views import RecordCreateView, RecordListView, RecordDetailView, RecordUpdateView, RecordDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', never_cache(RecordCreateView.as_view()), name='create'),
    path('', RecordListView.as_view(), name='list'),
    path('view/<int:pk>/', RecordDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', never_cache(RecordUpdateView.as_view()), name='edit'),
    path('delete/<int:pk>/', RecordDeleteView.as_view(), name='delete'),
]
