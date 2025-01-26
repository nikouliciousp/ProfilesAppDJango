from django.urls import include, path  # Import include and path for URL configuration
from rest_framework.routers import DefaultRouter  # Import DefaultRouter for automatic viewset routing

from .views import ProfileViewSet, ProfileStatusViewSet, AvatarUpdateViewSet  # Import viewsets

# Create a default router instance for registering viewsets
router = DefaultRouter()

# Register the ProfileViewSet with the router under the 'profiles' endpoint
# Assign a basename for generating consistent URL patterns for Profile-related operations
router.register(r'profiles', ProfileViewSet, basename='profile')

# Register the ProfileStatusViewSet with the router under the 'profile-status' endpoint
# Assign a basename for generating consistent URL patterns for ProfileStatus-related operations
router.register(r'profile-status', ProfileStatusViewSet, basename='profilestatus')

# Set the urlpatterns to handle the routing for API views
urlpatterns = [
    # Include all the automatically generated URLs by the router
    path("", include(router.urls)),

    # Add a specific endpoint for updating avatars using the AvatarUpdateViewSet
    path("avatar/", AvatarUpdateViewSet.as_view(), name="avatar-update"),
]
