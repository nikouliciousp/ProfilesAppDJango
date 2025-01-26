from profiles.models import Profile, ProfileStatus  # Import models
from rest_framework import mixins, viewsets, generics  # Import serializers here
from rest_framework.permissions import IsAuthenticated  # Import permission for authenticated users
from rest_framework.viewsets import ModelViewSet  # Import ModelViewSet for CRUD operations

from .permissions import IsOwnProfileOrReadOnly, IsOwnProfileStatusOrReadOnly  # Import custom permissions
from .serializers import ProfileSerializer, ProfileStatusSerializer, \
    ProfileAvatarSerializer  # Import serializers for Profile, ProfileStatus and ProfileAvatar
from rest_framework.filters import SearchFilter

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
    queryset = Profile.objects.all()

    # Serializer class to handle serialization and deserialization of Profile objects
    serializer_class = ProfileSerializer

    # Permission classes to ensure user authentication and restrict access
    permission_classes = [
        IsAuthenticated,
        IsOwnProfileOrReadOnly
    ]
    filter_backends = [SearchFilter]
    search_fields = ['user__username']


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
    serializer_class = ProfileStatusSerializer

    # Queryset to fetch all ProfileStatus objects from the database
    queryset = ProfileStatus.objects.all()

    # Permission classes to ensure user authentication and enforce ownership or admin access
    permission_classes = [
        IsAuthenticated,
        IsOwnProfileStatusOrReadOnly
    ]
    filter_backends = [SearchFilter]
    search_fields = ['status_text']

    def get_queryset(self):
        """
        Returns the queryset of ProfileStatus objects.

        If a 'username' query parameter is provided in the request, 
        the queryset is filtered to include only the ProfileStatus 
        objects associated with the specified username.

        Returns:
        - A queryset of ProfileStatus objects.
        """
        # Retrieve all ProfileStatus objects from the database
        queryset = super().get_queryset()

        # Get 'username' parameter from query params
        username = self.request.query_params.get('username', None)

        # If 'username' is provided, filter queryset by username
        if username:
            queryset = queryset.filter(user_profile__user__username=username)

        return queryset

    # Automatically associate the logged-in user's profile with the created status
    def perform_create(self, serializer):
        """
        Associates the logged-in user's profile with a new ProfileStatus 
        and prevents creation if a status already exists for the profile.
        """
        # Retrieve the profile of the logged-in user
        user_profile = self.request.user.profile

        # Save the new ProfileStatus with the associated user profile
        serializer.save(user_profile=user_profile)


class AvatarUpdateViewSet(generics.UpdateAPIView):
    """
    A viewset to handle profile avatar updates.

    Provides the following functionality:
    - Allows authenticated users to update their own avatar.

    Permissions:
    - The user must be authenticated.
    """

    # Serializer class to handle updating the avatar field
    serializer_class = ProfileAvatarSerializer

    # Permission classes to ensure the user is authenticated
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Retrieves the profile object of the currently authenticated user.

        Returns:
        - The profile object associated with the logged-in user.
        """
        return self.request.user.profile
