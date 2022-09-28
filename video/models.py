from django.db import models

from userprofile.models import Profile


class Video(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name="profile"
    )

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        db_table = "Video"

    def __str__(self):
        return f"video_{self.profile}"
