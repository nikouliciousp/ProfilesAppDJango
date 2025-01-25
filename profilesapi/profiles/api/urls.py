from rest_framework.routers import DefaultRouter

from .views import ProfileViewSet

# Create a default router instance for registering viewsets
router = DefaultRouter()

# Register the ProfileViewSet with the router under the 'profiles' endpoint
router.register('profiles', ProfileViewSet)

# Set the urlpatterns to the automatically generated URLs by the router
urlpatterns = router.urls
