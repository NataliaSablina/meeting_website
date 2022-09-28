from django.db import models

from userprofile.models import Profile


class Album(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name="profile"
    )
    name = models.CharField(max_length=250, verbose_name="name", null=True)
    photo = models.ImageField(
        upload_to="media/%Y/%m/%d/",
        verbose_name="photo",
        default="media/base_album_photo.png",
    )

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        db_table = "Album"

    def __str__(self):
        return f"album_{self.profile}"
