from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import CartItem, TransactionItem, Transaction
from .serializers import CartItemSerializer, CartSerializer, TransactionSerializer
from .permissions import IsCartOwner, IsCartItemOwner


class CartItemCreate(CreateAPIView):
  queryset = CartItem.objects.all()
  serializer_class = CartItemSerializer
  permission_classes = [IsAuthenticated]
  
  def perform_create(self, serializer):
    # Attach the user cart to the cart item
    
    serializer.save(cart=self.request.user.cart)
    

class CartItemRetrieveDelete(RetrieveDestroyAPIView):
  queryset = CartItem.objects.all()
  serializer_class = CartItemSerializer
  permission_classes = [IsAuthenticated, IsCartItemOwner]
   
   
class CartDetail(RetrieveAPIView):
  serializer_class = CartSerializer
  permission_classes = [IsAuthenticated, IsCartOwner]
  
  def get_object(self):
    return self.request.user.cart
  

class TransactionCreate(CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        cart_items = CartItem.objects.filter(cart=user.cart)
        total = 0
        for cart_item in cart_items:
            total += cart_item.book.price
        with transaction.atomic():
            transaction_instance = Transaction.objects.create(user=user, total=total)
            transaction_items = []
            for cart_item in cart_items:
                transaction_item = TransactionItem(transaction=transaction_instance, book=cart_item.book)
                transaction_items.append(transaction_item)
            TransactionItem.objects.bulk_create(transaction_items)
            
            # clear the user's cart
            request.user.cart.items.all().delete()

        serializer = self.serializer_class(transaction_instance, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
class TransactionList(ListAPIView):
  queryset = Transaction.objects.all()
  permission_classes = [IsAuthenticated, IsAdminUser]
  serializer_class = TransactionSerializer
