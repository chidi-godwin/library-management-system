from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from books.permissions import IsAdminOrReadOnly
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from .filters import BookFilter


@api_view(['GET'])
def index(request, format=None):
  return Response({
    'list or create books': reverse('books:book-list', request=request, format=format),
    'update, retrieve or delete book detials': reverse('books:book-detail', kwargs={'pk': 1}, request=request, format=format),
    'list or create categories': reverse('books:category-list', request=request, format=format),
    'update, retrieve or delete category detials': reverse('books:category-detail', kwargs={'pk': 1}, request=request, format=format)
  })

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    filterset_class = BookFilter


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
