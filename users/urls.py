from django.urls import path
from .views import SignUp, UserRetrieveUpdateDestroy, AdminUserUpdate, UserPasswordUpdate, api_root
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'users'

urlpatterns = format_suffix_patterns([
    path('', SignUp.as_view(), name='signup'),
    path('', UserRetrieveUpdateDestroy.as_view(), name='user-update'),
    path('index/', api_root, name='index'),
    path('admin-update/', AdminUserUpdate.as_view(), name='admin-update'),
    path('password/', UserPasswordUpdate.as_view(), name='password-update')
])
