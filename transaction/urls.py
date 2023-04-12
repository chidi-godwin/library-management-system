from django.urls import path
from .views import CartItemCreate, CartItemRetrieveDelete, CartDetail, TransactionCreate
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'transaction'

urlpatterns = format_suffix_patterns([
    path('cart_item/', CartItemCreate.as_view(), name='cart_item'),
    path('cart_item/<int:pk>/', CartItemRetrieveDelete.as_view(), name='cart_item_delete'),
    path('cart/', CartDetail.as_view(), name='cart-detail'),
    path('checkout/', TransactionCreate.as_view(), name='checkout'),
])
