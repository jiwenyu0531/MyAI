# coding: utf-8
from django.db import models
from django.utils.six import python_2_unicode_compatible
from gcmaster.models import Lyric


# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('gcmaster.Lyric',blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]

