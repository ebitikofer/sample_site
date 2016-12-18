from __future__ import unicode_literals

from django.db import models

class Link(models.Model):
    title = models.CharField(max_length=250)
    rating = models.CharField(max_length=250)
    thumbnail = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)

class File(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    rating = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    picture0 = models.CharField(max_length=1000)
    picture1 = models.CharField(max_length=1000)
    picture2 = models.CharField(max_length=1000)
    picture3 = models.CharField(max_length=1000)
    picture4 = models.CharField(max_length=1000)