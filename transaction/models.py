from django.db import models
from books.models import Book


class Cart(models.Model):
  user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='user_cart')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self) -> str:
    return f'Cart: {self.user.first_name} {self.user.last_name}'
  

class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  
class Transaction(models.Model):
  STATUS = (
    ('pending', 'pending'),
    ('approved', 'approved'),
    ('declined', 'declined')
  )
  
  status = models.CharField(max_length=10, choices=STATUS, default='pending')
  comments = models.TextField()
  total = models.DecimalField(max_digits=15, decimal_places=2)
  user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='transactions')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  

class TransactionItem (models.Model):
  transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='items')
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='transaction_items')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  