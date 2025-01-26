from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    """
    Profile model to extend the default User model with additional fields.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE  # Ensure the Profile is deleted when the related User is deleted
    )
    bio = models.TextField(
        max_length=500,
        null=True,
        blank=True  # Biography is optional
    )
    city = models.CharField(
        max_length=100,
        null=True,
        blank=True  # City is optional
    )
    avatar = models.ImageField(
        null=True,
        blank=True  # Avatar is optional
    )

    def __str__(self):
        # Returns the username from the associated User model
        return self.user.username


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,  # Deletes statuses when the linked Profile is deleted
        related_name="statuses"  # Enables reverse lookup (e.g., profile.statuses)
    )
    status_content = models.TextField(
        max_length=500,
        null=True,
        blank=True  # Status content is optional
    )
    created_at = models.DateTimeField(
        auto_now_add=True  # Automatically set when a status is created
    )
    updated_at = models.DateTimeField(
        auto_now=True  # Automatically update when a status is saved
    )

    def __str__(self):
        # Returns a string representation of the associated Profile
        return str(self.user_profile)
