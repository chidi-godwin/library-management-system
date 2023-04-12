from rest_framework import serializers
from .models import CartItem, Cart, TransactionItem, Transaction
from books.models import Book
from books.serializers import BookRetrieveSerializer


class CartItemSerializer(serializers.ModelSerializer):
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), source='book')
    cart_id = serializers.PrimaryKeyRelatedField(source='cart', read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'book_id', 'cart_id', 'created_at', 'updated_at']
        read_only_fields = ['cart_id', 'id', 'created_at', 'updated_at']

    def validate(self, attrs):
        print(attrs['book'].id)
        user = self.context['request'].user
        cart = user.cart
        book = attrs['book']

        if CartItem.objects.filter(cart=cart, book=book).exists():
            raise serializers.ValidationError(
                'This book is already in the cart.')
        return attrs


class CartItemRetrieveSerializer(serializers.ModelSerializer):
    book = BookRetrieveSerializer(read_only=True)
    cart_id = serializers.PrimaryKeyRelatedField(source='cart', read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'book', 'cart_id']
        read_only_fields = ['cart_id', 'id']


class CartSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    items = CartItemRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user_id', 'items']


class TransactionItemSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = TransactionItem
        fields = ['id', 'book', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class TransactionSerializer(serializers.ModelSerializer):
    items = TransactionItemSerializer(many=True, read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'status', 'comments', 'total',
                  'user', 'created_at', 'updated_at', 'items']
        read_only_fields = ['id', 'status', 'comments',
                            'total', 'user', 'created_at', 'updated_at', 'items']


class TransactionApproveSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Transaction.STATUS, required=True)
    comments = serializers.CharField(required=False)

    class Meta:
        model = Transaction
        fields = ['id', 'status', 'comments', 'total',
                  'user', 'created_at', 'updated_at', 'items']
        read_only_fields = ['id', 'total', 'user',
                            'created_at', 'updated_at', 'items']
