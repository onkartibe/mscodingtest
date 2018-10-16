# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    slug = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        ordering = ('created',)