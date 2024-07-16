from django import template
from blog.models import Post


register = template.Library()


@register.inclusion_tag("website-latest-post.html")
def latest_posts(arg=6):
    posts = Post.objects.filter(status=True).order_by("-id")[0:arg]
    return {"posts": posts}
