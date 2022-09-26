from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from user.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model"""

    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    creation_date = models.DateTimeField(
        verbose_name="creation",
        auto_now_add=True,
        auto_now=False,
        blank=True,
        null=True,
    )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "User"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
