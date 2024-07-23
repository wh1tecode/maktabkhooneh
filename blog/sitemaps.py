from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from django.urls import reverse
from blog.models import Post

class BlogSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self, obj) -> str:
        return reverse(viewname="blog:single", kwargs={"pid": obj.id})