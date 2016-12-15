from __future__ import unicode_literals

from django.db import models

class Link(models.Model):
    title = models.CharField(max_length=250)
    rating = models.CharField(max_length=250)
    thumbnail = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)