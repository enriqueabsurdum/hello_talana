"""User Register view."""

# Python
import random

# Django REST framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from apps.users.api.serializers import (
    UserModelSerializer, UserRegisterSerializer,
    UserLoginSerializer, UserCheckSerializer
)

# Models
from apps.users.models import User


class UserGenericViewSet(viewsets.GenericViewSet):
    """User Generic ViewSet class.
    More information: https://github.com/encode/django-rest-framework/blob/master/rest_framework/viewsets.py
    """

    @action(detail=False, methods=['post'])
    def login(self, request) -> Response:
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'access_token': token,
            'user': UserModelSerializer(user).data
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def register(self, request) -> Response:
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = {
            'user': UserModelSerializer(user).data
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def check(self, request) -> Response:
        serializer = UserCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'message': 'La dirección de correo electrónico ha sido verificada'
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def generate_password(self, request) -> Response:
        data = {}
        return Response(data, status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def winner(self, request) -> Response:
        user_ids = User.objects.filter(is_verified=True).values('id')
        data = {
            'winner': 'Ningún ganador',
            'value': False
        }

        if len(user_ids) > 0:
            random_id = random.choice(user_ids)['id']
            try:
                user = User.objects.get(pk=random_id)
                serializer = UserModelSerializer(user)
                data = {
                    'winner': serializer.data,
                    'value': True
                }
            except User.DoesNotExist:
                user = None
        return Response(data, status.HTTP_200_OK)
