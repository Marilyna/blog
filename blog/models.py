from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    categories = models.ManyToManyField('Category', related_name='posts')

    @property
    def photos_count(self):
        return self.images.count()

    def __unicode__(self):
        return ', '.join([str(self.id), self.title])


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    post = models.ForeignKey(Post, related_name='images')
