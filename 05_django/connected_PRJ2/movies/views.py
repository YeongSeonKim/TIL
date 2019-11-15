# from hashlib
from itertools import chain
from IPython import embed
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Rating
from .forms import MovieForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request, 'movies/index.html', context)  

def new(request):
    pass

@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        # embed()

        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()

        return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
        context = {
            'form':form,
        }
        return render(request, 'movies/create.html', context)


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    person = get_object_or_404(get_user_model())
    context = {
        'movie':movie,
        'person':person,
    }
    return render(request, 'movies/detail.html', context)


@login_required
def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                movie = form.save()

                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:index')


@require_POST
def delete(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        if request.user == movie.user:
            movie.delete()
        else:
            return render('movies:detail', movie.pk)
        return redirect('movies:index')


def comments_create(requset):
    pass

def comments_delete(request):
    pass
