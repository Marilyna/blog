from django.contrib import admin
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'pub_date', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
