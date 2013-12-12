from django.contrib import admin
from blog.models import Post, Category, Image


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'published')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
