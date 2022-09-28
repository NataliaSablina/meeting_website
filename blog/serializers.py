from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('blog', 'content', 'quiz')

    def create(self, validated_data):
        return Post(**validated_data)

    def update(self):
        pass
