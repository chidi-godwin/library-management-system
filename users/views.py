from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from transaction.models import Cart


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
    
    