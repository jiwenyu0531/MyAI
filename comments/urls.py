from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/lyric/(?P<lyric_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]