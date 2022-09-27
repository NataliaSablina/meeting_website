from rest_framework.generics import get_object_or_404

from user.models import CustomUser


def get_available_users():
    return CustomUser.objects.all()


def get_current_user_by_email(pk):
    print(pk)
    user = get_object_or_404(CustomUser.objects.get(pk=pk))
    return user
