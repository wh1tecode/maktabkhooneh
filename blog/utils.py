from .models import Post


def next_prev_post(post: Post, posts: list[Post]) -> tuple:
    posts = list(posts)
    total_index = len(posts) - 1
    print(total_index)
    current_post_index = posts.index(post)
    prev_post_index = current_post_index - 1
    next_post_index = current_post_index + 1
    prev_post = None if prev_post_index < 0 else posts[prev_post_index]
    next_post = None if next_post_index > total_index else posts[next_post_index]
    return (prev_post, next_post)


def increase_post_visits(post: Post):
    post.counted_views += 1
    Post.objects.filter(pk=post.pk).update(counted_views=post.counted_views)

