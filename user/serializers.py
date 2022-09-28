from rest_framework import serializers

from album.models import Album
from blog.models import Blog
from form.models import Form
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
        Blog.objects.create(id=user.pk, profile=profile)
        Form.objects.create(id=user.pk, profile=profile)
        Album.objects.create(id=user.pk, profile=profile, name="It's me")
        print(profile.pk)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email",)
