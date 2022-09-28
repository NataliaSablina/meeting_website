from rest_framework import routers

from blog.views import PostViewSet

router = routers.SimpleRouter()
router.register(r"blog", PostViewSet)


urlpatterns = []
urlpatterns += router.urls
