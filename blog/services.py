from blog.models import Post


def get_available_posts():
    return Post.objects.all()