from django.urls import path
from .views import CartItemListCreate


urlpatterns = [
  path('cart_item', CartItemListCreate.as_view(), name='cart_item')
]