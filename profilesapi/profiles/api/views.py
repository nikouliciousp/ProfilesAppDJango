from profiles.models import Profile, ProfileStatus  # Import models
from rest_framework import mixins, viewsets, serializers  # Import serializers here
from rest_framework.permissions import IsAuthenticated  # Import permission for authenticated users
from rest_framework.viewsets import ModelViewSet  # Import ModelViewSet for CRUD operations

from .permissions import IsOwnProfileOrReadOnly, IsOwnProfileStatusOrReadOnly  # Import custom permissions
from .serializers import ProfileSerializer, ProfileStatusSerializer  # Import serializers for Profile and ProfileStatus


class ProfileViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    A viewset for handling Profile operations.

    Provides the following actions:
    - Retrieve a specific profile.
    - List all profiles.
    - Update a profile (only if it's the user's own profile or by an admin).

    Permissions:
    - The user must be authenticated.
    - Admins can update any profile; regular users can only update their own profile.
    """

    # Queryset to fetch all Profile objects from the database
    queryset = Profile.objects.all()  # Retrieve all Profile objects from the database.

    # Serializer class to handle serialization and deserialization of Profile objects
    serializer_class = ProfileSerializer  # Serialize and deserialize Profile objects.

    # Permission classes to ensure user authentication and restrict access
    permission_classes = [
        IsAuthenticated,  # Ensure the user is authenticated.
        IsOwnProfileOrReadOnly  # Allow updates only if the user owns the profile or is an admin.
    ]


class ProfileStatusViewSet(ModelViewSet):
    """
    A viewset for handling ProfileStatus operations.

    Provides the following actions:
    - Create a new profile status.
    - Retrieve an existing profile status.
    - Update a profile status (only if it belongs to the user or by an admin).
    - Delete a profile status.

    Permissions:
    - The user must be authenticated.
    - Admins can modify or delete any profile status; regular users can only modify or delete their own profile status.
    """

    # Serializer class to handle serialization and deserialization of ProfileStatus objects
    serializer_class = ProfileStatusSerializer  # Serialize and deserialize ProfileStatus objects.

    # Queryset to fetch all ProfileStatus objects from the database
    queryset = ProfileStatus.objects.all()  # Retrieve all ProfileStatus objects from the database.

    # Permission classes to ensure user authentication and enforce ownership or admin access
    permission_classes = [
        IsAuthenticated,  # Ensure the user is authenticated.
        IsOwnProfileStatusOrReadOnly  # Allow updates only if the user owns the status or is an admin.
    ]

    # Automatically associate the logged-in user's profile with the created status
    def perform_create(self, serializer):
        # Retrieve the profile of the logged-in user
        user_profile = self.request.user.profile

        # Check if a ProfileStatus already exists for the logged-in user's profile
        if ProfileStatus.objects.filter(user_profile=user_profile).exists():
            # If a status already exists, raise a validation error
            raise serializers.ValidationError("A status already exists for this profile.")

        # Save the new ProfileStatus with the associated user profile
        serializer.save(user_profile=user_profile)
