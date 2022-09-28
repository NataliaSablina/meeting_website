from django.contrib import admin

from blog.models import PostComment, Post, Blog

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(PostComment)
