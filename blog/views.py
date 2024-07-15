from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Post
from .utils import increase_post_visits

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(status=True, published_date__lt=datetime.utcnow())
    context = {"posts": posts}
    return render(request, "blog-home.html", context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid)
    increase_post_visits(post)
    context = {"post": post}
    return render(request, "blog-single.html", context)