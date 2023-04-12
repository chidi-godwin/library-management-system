from django.urls import path, include
from rest_framework_simplejwt import views
from .views import index

app_name = 'Auth'

urlpatterns = [
  path('index/', index, name='index'),
  path('signin/', views.TokenObtainPairView.as_view(), name='login'),
  path('refresh/', views.TokenRefreshView.as_view(), name='refresh'),
  path('verify/', views.TokenVerifyView.as_view(), name="verify"),
  path('', include('djoser.urls')),
  path('', include('djoser.urls.jwt')),
]