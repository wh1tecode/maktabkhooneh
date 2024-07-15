from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .utils import increase_post_visits

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(status=True, published_date__lt=timezone.now())
    context = {"posts": posts}
    return render(request, "blog-home.html", context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=True, published_date__lt=timezone.now())
    post = get_object_or_404(posts, pk=pid)
    increase_post_visits(post)
    context = {"post": post}
    return render(request, "blog-single.html", context)