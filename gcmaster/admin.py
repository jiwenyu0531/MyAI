from django.contrib import admin
from .models import Lyric, Category, Tag, Author


class LyricAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender']


admin.site.register(Lyric, LyricAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author, AuthorAdmin)

