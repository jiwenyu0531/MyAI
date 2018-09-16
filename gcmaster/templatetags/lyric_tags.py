from gcmaster.models import Lyric, Category, Author
from django import template

register = template.Library()


@register.simple_tag
def get_recent_lyric(num=5):
    return Lyric.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_hot_author(num=5):
    return Author.objects.all()[:num]


@register.simple_tag
def archives():
    return Lyric.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()


