"""User apps."""

# Django
from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    """User app config."""

    name = 'apps.users'
    verbose_name = 'User'
    verbose_name_plural = 'Users'
