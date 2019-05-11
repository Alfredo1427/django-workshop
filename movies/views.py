from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from movies.forms import MovieForm
from movies.models import Movie


# Create a new movie
def movie_create(request):
    movie_form = MovieForm()

    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            messages.success(request, '{}'.format('Película guardada exitosamente'))
            return redirect(movie_list)
        else:
            print(movie_form.errors)
    return render(request, 'movies/movie_create.html', {'movie_form': movie_form})


# List existing movies
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})


# Get movie detail
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})


# Delete movie
def movie_delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    messages.success(request, '{}'.format('Película eliminada exitosamente'))
    return redirect(movie_list)
