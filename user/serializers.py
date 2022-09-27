from rest_framework import serializers

from user.models import CustomUser


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email", "password")

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email",)
