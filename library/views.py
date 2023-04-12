from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
  return Response({
    'Auth': reverse('Auth:index', request=request, format=format),
    'users': reverse('users:index', request=request, format=format),
    'books': reverse('books:index', request=request, format=format),
    'transaction': reverse('transaction:cart_item', request=request, format=format)
  })