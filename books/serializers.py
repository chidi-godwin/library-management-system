from rest_framework import serializers
from .models import Book, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=True,
        source='category'
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'quantity', 'category_id']
        read_only_fields = ['id']
        

class BookRetrieveSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        fields = ['id', 'title', 'price', 'category']
        model = Book


