from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'content', 'pub_date', ]
    list_display = ('author', 'title', 'content', 'pub_date', )


admin.site.register(Post, PostAdmin)
