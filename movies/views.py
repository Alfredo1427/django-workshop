from django.shortcuts import render

# Create your views here.
from movies.forms import MovieForm
from movies.models import Movie


# Create a new movie
def movie_create(request):
    movie_form = MovieForm()
    return render(request, 'movies/movie_create.html', {'movie_form': movie_form})


# List existing movies
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})


# Get movie detail
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})
