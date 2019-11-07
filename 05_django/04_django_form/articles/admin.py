from django.contrib import admin
from .models import Article
from .models import Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'article', 'content', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)