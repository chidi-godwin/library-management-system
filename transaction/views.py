from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import CartItem, Cart
from .serializers import CartItemSerializer, CartSerializer
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
  

class Transaction(CreateAPIView):
  pass