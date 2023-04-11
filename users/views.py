from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer, UserUpdateSerializer, AdminUserUpdate, UserPasswordUpdate
from .permissions import IsOwner
from transaction.models import Cart

@api_view(['GET'])
def api_root(request, format=None):
  return Response({
    'signup': reverse('users:signup', request=request, format=format),
    'update, retrieve or delete user detials': reverse('users:user-update', request=request, format=format),
    'make user admin': reverse('users:admin-update', request=request, format=format),
    'change user password': reverse('users:password-update', request=request, format=format)
  })

class SignUp(generics.CreateAPIView):
  queryset = User
  serializer_class = UserSerializer
  
  def perform_create(self, serializer):
    # create the user
    user = serializer.save()
    
    # create a default cart for each user
    cart = Cart.objects.create(user=user)
    
    # return the user object
    return user
    

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = User
  serializer_class = UserUpdateSerializer
  permission_classes = [IsAuthenticated, IsOwner]
  
  def get_object(self):
    return self.request.user
  
class AdminUserUpdate(generics.UpdateAPIView):
  queryset = User
  serializer_class = AdminUserUpdate
  permission_classes = [IsAuthenticated, IsAdminUser]

  
class UserPasswordUpdate(generics.UpdateAPIView):
  queryset = User
  serializer_class = UserPasswordUpdate
  permission_classes = [IsAuthenticated, IsOwner]
  
  def get_object(self):
    return self.request.user