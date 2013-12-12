from django.contrib.auth.models import User
from django.db import models

from multifilefield.models import MultiFileField


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    categories = models.ManyToManyField('Category', related_name='posts')
    # images = MultiFileField(upload_to='images/%Y/%m/%d


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    post = models.ForeignKey(Post)