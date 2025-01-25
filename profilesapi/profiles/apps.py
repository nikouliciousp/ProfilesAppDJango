from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the 'profiles' app.
    This handles the app-specific settings and initialization.
    """
    default_auto_field = 'django.db.models.BigAutoField'  # Sets the default type for primary keys.
    name = 'profiles'  # Specifies the name of the app.

    def ready(self):
        """
        Import and set up signal handlers when the app is ready.
        """
        import profiles.signals
