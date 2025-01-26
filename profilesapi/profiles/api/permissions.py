from rest_framework import permissions


class IsOwnProfileOrReadOnly(permissions.BasePermission):
    """Allows user to edit their own profile or admin to edit all profiles"""

    def has_object_permission(self, request, view, obj):
        """Check if the user has permission to perform actions on a specific object"""
        # Allow read-only methods (GET, HEAD, OPTIONS) for any user
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow actions if the user is the owner of the profile or is an admin
        return hasattr(obj, 'user') and (obj.user == request.user or request.user.is_staff)


class IsAdminOrReadOnly(permissions.BasePermission):
    """Allows access to edit profiles for admins only, read-only for others"""

    def has_permission(self, request, view):
        """Check if the user has permission to access the view"""
        # Allow actions only if the user is authenticated and is an admin
        return request.method in permissions.SAFE_METHODS or (
                request.user and request.user.is_authenticated and request.user.is_staff
        )


class IsOwnProfileStatusOrReadOnly(permissions.BasePermission):
    """Allows user to edit their own profile status or admin to edit all profiles"""

    def has_object_permission(self, request, view, obj):
        """Check if the user has permission to perform actions on a specific object"""
        # Allow read-only methods (GET, HEAD, OPTIONS) for any user
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow actions if the user owns the profile status or is an admin
        return hasattr(obj, 'user_profile') and (
                obj.user_profile.user == request.user or request.user.is_staff
        )
