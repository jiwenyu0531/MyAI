# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样。
    再次强调一定要继承 models.Model 类！
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class Lyric(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    body = models.TextField()

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 摘要
    excerpt = models.CharField(max_length=200, blank=True)

    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    category = models.ForeignKey(Category,null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)

    # 歌词作者
    author = models.ForeignKey(Author,null=True, blank=True, on_delete=models.SET_NULL)

    # 由谁发布的
    addedby = models.ForeignKey(User,null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gcmaster:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']

