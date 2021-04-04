"""User Register serializer."""

# Python
from datetime import timedelta

# PyJWT
import jwt

# Django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import password_validation

# Django REST framework
from django.template.loader import render_to_string
from django.utils import timezone
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from apps.users.models import User

# Tasks
from apps.users.tasks import send_confirmation_email


class UserRegisterSerializer(serializers.Serializer):
    """User Register Serializer class."""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    first_name = serializers.CharField(min_length=2, max_length=150)
    last_name = serializers.CharField(min_length=2, max_length=150)
    password = serializers.CharField(min_length=8, max_length=128)

    def validate(self, data):
        password = data['password']
        password_validation.validate_password(password)
        return data

    def create(self, data):
        user = User.objects.create_user(**data, is_verified=False)
        send_confirmation_email.delay(user_pk=user.id)
        return user
