from rest_framework import serializers

from blog.models import Blog
from user.models import CustomUser
from userprofile.models import Profile


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email", "password")

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        profile = Profile.objects.create(id=user.pk, user=user)
        blog = Blog.objects.create(id=user.pk, profile=profile)
        print(profile.pk)
        print(blog.pk)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email",)
