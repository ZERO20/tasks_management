from rest_framework.permissions import AllowAny
from rest_framework import mixins, viewsets

from django.contrib.auth.models import User

from apps.users.serializers.v1.user import UserSerializer


class CreateUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Create User"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]
