from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to create or update books.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Allow read-only access for all users
            return True

        # Only allow admins to create or update books
        return request.user and request.user.is_authenticated and request.user.is_staff == True
