from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from gcmaster.models import Lyric, Category
import markdown
from comments.forms import CommentForm


def index(request):
    lyric_list = Lyric.objects.all().order_by('-created_time')
    return render(request, 'gcmaster/index.html', context={'lyric_list': lyric_list})


def detail(request, pk):
    lyric = get_object_or_404(Lyric, pk=pk)
    lyric.body = markdown.markdown(lyric.body, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = lyric.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'lyric': lyric,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'gcmaster/detail.html', context=context)


'''
按歌手查询歌词
'''
def author_archives(request, pk):
    lyric_list = Lyric.objects.filter(author_id__in=pk)
    return render(request, 'gcmaster/index.html', context={'lyric_list': lyric_list})


def archives(request, year, month):
    lyric_list = Lyric.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'gcmaster/index.html', context={'lyric_list': lyric_list})


def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    lyric_list = Lyric.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'gcmaster/index.html', context={'lyric_list': lyric_list})