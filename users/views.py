from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class SignUp(generics.CreateAPIView):
  queryset = User
  serializer_class = UserSerializer
  