from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('published')
    author = models.ForeignKey(User)
    categories = models.ManyToManyField('Category', related_name='posts')


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.title