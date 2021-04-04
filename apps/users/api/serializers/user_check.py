"""User Check serializer."""

# Django
from django.conf import settings

# Django REST framework
from rest_framework import serializers

# PyJWT
import jwt

from apps.users.models import User


class UserCheckSerializer(serializers.Serializer):
    """User Check Serializer class."""

    token = serializers.CharField()

    def validate_token(self, data):
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('El enlace de verificación ha caducado.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Token inválido.')

        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Token inválido.')

        self.context['payload'] = payload
        return data

    def save(self, **kwargs):
        payload = self.context['payload']
        user = User.objects.get(email=payload['user'])
        user.is_verified = True
        user.save()
