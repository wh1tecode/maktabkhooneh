from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "published_date"
    empty_value_display = "-empty-"
    list_display = (
        "title",
        "counted_views",
        "status",
        "published_date",
        "created_date",
    )
    list_filter = ('status',)
    search_fields = ['title','content']
