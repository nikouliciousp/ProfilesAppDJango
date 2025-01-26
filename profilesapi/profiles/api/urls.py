from rest_framework.routers import DefaultRouter

from .views import ProfileViewSet, ProfileStatusViewSet

# Create a default router instance for registering viewsets
router = DefaultRouter()

# Register the ProfileViewSet with the router under the 'profiles' endpoint
# Add a basename for consistent URL lookups related to profiles
router.register(r'profiles', ProfileViewSet, basename='profile')

# Register the ProfileStatusViewSet with the router under the 'profile-status' endpoint
# Add a basename for consistent URL lookups related to profile statuses
router.register(r'profile-status', ProfileStatusViewSet, basename='profilestatus')

# Set the urlpatterns to the automatically generated URLs by the router
# The router will handle the URL patterns for the registered viewsets automatically
urlpatterns = router.urls
