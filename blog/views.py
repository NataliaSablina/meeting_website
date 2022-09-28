from rest_framework.viewsets import ModelViewSet

from blog.serializers import PostSerializer
from blog.services import get_available_posts


class PostViewSet(ModelViewSet):
    queryset = get_available_posts()
    serializer_class = PostSerializer
