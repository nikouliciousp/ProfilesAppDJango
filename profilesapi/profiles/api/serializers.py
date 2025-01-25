from profiles.models import Profile, ProfileStatus
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    This serializer includes all fields of the Profile model
    and makes the 'user' and 'avatar' fields read-only.
    """

    # Read-only representation of the user field using the related object's string representation
    user = serializers.StringRelatedField(read_only=True)  # The user field is represented as a string and is read-only

    # Read-only representation of the avatar field, which is an image
    avatar = serializers.ImageField(read_only=True)  # The avatar field is read-only and represents an image

    class Meta:
        model = Profile  # Specifies the model the serializer is for
        fields = "__all__"  # Includes all fields of the Profile model in the serialization


class ProfileStatusSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProfileStatus model.
    This serializer includes all fields of the ProfileStatus model
    and makes the 'user_profile' field read-only.
    """

    # Read-only representation of the user_profile field using the related object's string representation
    user_profile = serializers.StringRelatedField(
        read_only=True)  # The user_profile field is represented as a string and is read-only

    class Meta:
        model = ProfileStatus  # Specifies the model the serializer is for
        fields = "__all__"  # Includes all fields of the ProfileStatus model in the serialization


class ProfileAvatarSerializer(serializers.ModelSerializer):
    """
    Serializer to handle profile avatar updates and retrieval.
    This serializer includes only the avatar field.
    """

    class Meta:
        model = Profile  # Specifies the model the serializer is for
        fields = ('avatar',)  # Includes only the avatar field in the serialization
