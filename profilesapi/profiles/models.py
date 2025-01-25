from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    """
    Profile model to extend the default User model with additional fields.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links Profile to a single User instance
    bio = models.TextField(max_length=500, null=True, blank=True)  # Short biography of the user
    city = models.CharField(max_length=100, null=True, blank=True)  # User's city
    avatar = models.ImageField(null=True, blank=True)  # Profile picture of the user

    def __str__(self):
        # Returns the username associated with this profile
        return self.user.username


class ProfileStatus(models.Model):
    """
    ProfileStatus model to store user status updates linked to their profile.
    """
    user_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)  # Links Status to a single Profile
    status_content = models.TextField(max_length=500, null=True, blank=True)  # User's status or message
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the status was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the status was last updated

    def __str__(self):
        # Returns a string representation of the linked user profile
        return str(self.user_profile)
