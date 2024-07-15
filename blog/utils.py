from .models import Post

def increase_post_visits(post: Post):
    post.counted_views += 1
    Post.objects.filter(pk=post.pk).update(counted_views=post.counted_views)
