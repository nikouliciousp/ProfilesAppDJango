from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal handler to automatically create a Profile object 
    whenever a new User instance is created.

    Args:
        sender (Model): The model class sending the signal (User in this case).
        instance (User): The instance of the User model that triggered the signal.
        created (bool): A boolean indicating whether a new record was created.
        **kwargs: Additional keyword arguments passed by the signal.
    """
    print('Creating Profile', created)
    if created:
        Profile.objects.create(user=instance)
