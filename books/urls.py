from django.urls import path
from .views import AuthorDetailView, AuthorListCreateView, BookByAuthorListView, BookByCategoryListView, BookDetailView, BookListCreateView, CategoryDetailView, CategoryListCreateView


urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(),
         name='category-detail'),
    path('authors/<int:author_id>/books/',
         BookByAuthorListView.as_view(), name='books-by-author'),
    path('categories/<int:category_id>/books/',
         BookByCategoryListView.as_view(), name='books-by-category'),
]
