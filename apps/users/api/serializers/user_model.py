"""User Model serializer."""

# Django REST framework
from rest_framework import serializers

# Models
from apps.users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    """User Model Serializer class."""

    class Meta:
        model = User
        fields = (
            'email', 'first_name', 'last_name'
        )
