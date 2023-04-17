from django_filters import rest_framework as filters
from .models import Book


class BookFilter(filters.FilterSet):
    price__gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
    title = filters.CharFilter(field_name='title', lookup_expr='exact')
    category_name = filters.CharFilter(field_name='category__name')
    category_id = filters.NumberFilter(field_name='category__id')
    author = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['price', 'title', 'category', 'author']
