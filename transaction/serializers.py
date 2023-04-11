from rest_framework import serializers
from .models import CartItem, Cart
from books.models import Book


class CartItemSerializer(serializers.ModelSerializer):
  book_id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), source='book')
  cart_id = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all(), source='cart')
  id = serializers.PrimaryKeyRelatedField(queryset=CartItem.objects.all(), source='id')

  class Meta:
    model = CartItem
    fields = ['book_id', 'cart_id', 'id', 'created_at', 'updated_at']
    read_only_fields = ['cart_id', 'id', 'created_at', 'updated_at']
    