from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from base.serializers import ResetPasswordSerializer
from user.permissions import IsSelf
from user.serializers import UserCreateSerializer, UserSerializer
from user.services import get_available_users


class UserViewSet(ModelViewSet):
    queryset = get_available_users()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserCreateSerializer
        return UserSerializer

    @action(detail=True, methods=["post"], permission_classes=[IsAdminUser | IsSelf])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data["password1"])
            user.save()
            return Response({"status": "password set"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
