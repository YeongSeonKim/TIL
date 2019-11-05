from django.contrib import admin
from .models import Movie
from .models import Comment

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
        list_display = (
            'pk', 'title', 'title_en', 'audience', 'open_date',
            'genre', 'watch_grade', 'score', 'poster_url', 'description',
        )

class CommentAdmin(admin.ModelAdmin):
    list_display= (
        'pk', 'content', 'movie', 'created_at', 'updated_at',
    )

admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment, CommentAdmin)