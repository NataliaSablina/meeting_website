from rest_framework import routers
from django.urls import path, include
from user.views import UserViewSet

router = routers.SimpleRouter()
router.register(r"user", UserViewSet)


urlpatterns = [
    path("authentication/", include("rest_framework.urls"), name="authentication")
]
urlpatterns += router.urls
