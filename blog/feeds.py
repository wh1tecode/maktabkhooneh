from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "Post news"
    link = "/rss/feed"
    description = "best post"

    def items(self):
        return Post.objects.filter(status=True)

    def item_title(self, item):
        return item.content[0:100]

    def item_description(self, item):
        return item.title