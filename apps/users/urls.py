"""Users URLs."""

# Django
from django.urls import path, include

# Django REST framework
from rest_framework.routers import DefaultRouter

# Views
from .api import views as user_views

router = DefaultRouter()
router.register(r'users', user_views.UserGenericViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
