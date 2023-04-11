from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import CartItem
from .serializers import CartItemSerializer


class CartItemListCreate(ListCreateAPIView):
  queryset = CartItem.objects.all()
  serializer_class = CartItemSerializer
  permission_classes = [IsAuthenticated]
  
  def perform_create(self, serializer):
    # Attach the user cart to the cart item
    
    serializer.save(cart=self.request.user.cart)