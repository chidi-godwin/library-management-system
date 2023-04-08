from rest_framework import generics
from .models import Author, Book, Category
from .serializers import AuthorSerializer, BookSerializer, CategorySerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookByAuthorListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author_id = self.kwargs.get('author_id')
        return Book.objects.filter(authors__id=author_id)

class BookByCategoryListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Book.objects.filter(category__id=category_id)