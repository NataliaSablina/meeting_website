from django.db import models

from user.models import CustomUser


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="user", unique=True)
    # form = models.CharField(verbose_name="form", blank=True, null=True)
    # album = models.CharField(verbose_name="album", blank=True, null=True)
    # video = models.CharField(verbose_name="video", blank=True, null=True)
    # interest = models.CharField(verbose_name="interest", blank=True, null=True)
    # blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, verbose_name='blog')
    # location = models.CharField(verbose_name="location", blank=True, null=True)
    # self_portrait = models.CharField(verbose_name="self_portrait", blank=True, null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        db_table = "Profile"

    def __str__(self):
        return f"{self.user}_profile"
