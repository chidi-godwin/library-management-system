from django.urls import path
from .views import BookDetailView, BookListCreateView, CategoryDetailView, CategoryListCreateView, index
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'books'

urlpatterns = format_suffix_patterns([
    path('', BookListCreateView.as_view(), name='book-list'),
    path('index/', index, name='index'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(),
         name='category-detail'),
])
