from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from base.serializers import ResetPasswordSerializer
from user.serializers import UserCreateSerializer, UserSerializer
from user.services import get_available_users, get_current_user_by_email


class UserViewSet(ModelViewSet):
    queryset = get_available_users()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserCreateSerializer
        return UserSerializer
