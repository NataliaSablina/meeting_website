from django.db import models

from user.models import CustomUser
from userprofile.models import Profile


class Blog(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, verbose_name="profile", unique=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        db_table = "Blog"

    def __str__(self):
        return f"blog_{self.profile}"


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="blog")
    content = models.TextField(verbose_name="content")
    quiz = models.CharField(verbose_name="quiz", blank=True, null=True, max_length=250)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        db_table = "Post"

    def __str__(self):
        return f"{self.blog}_post_{self.pk}"


class PostComment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, verbose_name="user", null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="post")
    content = models.TextField(verbose_name="content")
    comment = models.ForeignKey('PostComment', on_delete=models.CASCADE, verbose_name="comment_on_comment")

    class Meta:
        verbose_name = "PostComment"
        verbose_name_plural = "PostComments"
        db_table = "PostComment"

    def __str__(self):
        return f"{self.post}_comment_{self.pk}"

