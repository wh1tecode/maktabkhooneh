from django import template
from django.template.loader import get_template
from blog.models import Post, Category, Comment
from django.db.models import Count

register = template.Library()

@register.simple_tag(name="total_posts")
def total_posts():
    posts = Post.objects.filter(status=True)
    return posts

@register.simple_tag(name="total_posts_count")
def total_posts_count():
    posts_count = Post.objects.filter(status=True).count()
    return posts_count

@register.filter(name="sniped")
def sniped_content(value, arg=20):
    return value[0:arg] + "..."

@register.filter(name="postcommentscount")
def post_comments_count(post: Post):
    return Comment.objects.filter(approve=True, post=post).count()

@register.inclusion_tag("blog-popular-post.html")
def popular_posts(arg=3):
    posts = Post.objects.filter(status=True).order_by("-counted_views")[0:arg]
    return {"posts": posts}

@register.inclusion_tag("blog-post-categories.html")
def post_categories():
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    cat_dict = {}
    for cat in categories:
        cat_dict[cat.name] = posts.filter(category=cat).count()
    print(cat_dict)
    return {"categories": cat_dict}

@register.inclusion_tag("blog-post-categories.html")
def latest_posts(arg=6):
    posts = Post.objects.filter(status=True).latest("id")[arg]
    return {"posts": posts}

# register.inclusion_tag(get_template("blog-popular-post.html"))(popular_posts)