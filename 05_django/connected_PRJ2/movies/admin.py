from django.contrib import admin
from .models import Movie, Rating

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'poster', 'created_at', 'updated_at', 'user',)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('score', 'content', 'created_at', 'updated_at', 'user',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
