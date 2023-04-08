from rest_framework import serializers
from .models import Book, Category, Author


class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'price', 'category_id',
                  'author_id', 'quantity')


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'books')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
