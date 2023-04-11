from django.db import models
from users.models import User
from books.models import Book


class Cart(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  

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
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  

class TransactionItem (models.Model):
  transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='items')
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='transaction_items')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  