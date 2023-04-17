from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def index(request, format=None):
  return Response({
    'Login (Create JWT Token)' : reverse('Auth:login', request=request, format=format),
    'Refresh JWT Token': reverse('Auth:refresh', request=request, format=format),
    'Verify Token': reverse('Auth:verify', request=request, format=format)
  })
