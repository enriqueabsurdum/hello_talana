"""User model."""

# Django
from django.contrib.auth.models import AbstractUser
from django.db import models

# Core
from apps.core.models import BaseModel

# Managers
from apps.users.managers.user_manager import UserManager


class User(BaseModel, AbstractUser):
    """User class.
    More information: https://github.com/django/django/blob/main/django/contrib/auth/models.py
    """

    username = None
    email = models.EmailField(
        verbose_name='email address',
        unique=True,
        error_messages={
            'unique': (
                'Ya existe un usuario con esa dirección de correo electrónico.'
            )
        }
    )
    is_verified = models.BooleanField(
        verbose_name='verified',
        default=False,
        help_text=(
            'Establecer en verdadero cuando el usuario haya verificado su '
            'dirección de correo electrónico.'
        )
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email
