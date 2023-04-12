from rest_framework import serializers
from .models import Book, Category


class BookSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=True,
        source='category'
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'quantity', 'category_id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
