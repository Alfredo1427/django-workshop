from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from movies.forms import MovieForm
from movies.models import Movie


# Create a new movie
def movie_create_or_edit(request, pk=None):
    # Views for retrieving existing or new modelform
    if request.method == 'GET':
        if pk:
            print('GET movie with pk')
            movie = Movie.objects.get(pk=pk)
            movie_form = MovieForm(instance=movie)
        else:
            movie_form = MovieForm()

    # Views for retrieving existing or new modelform
    if request.method == 'POST':
        if pk:
            print('POST movie with pk')
            movie = Movie.objects.get(pk=pk)
            movie_form = MovieForm(request.POST, instance=movie)
        else:
            movie_form = MovieForm(request.POST)

        if movie_form.is_valid():
            movie_form.save()
            messages.success(request, '{}'.format('Película guardada exitosamente'))
            return redirect(movie_list)
        else:
            for error in movie_form.errors:
                print(error)
    return render(request, 'movies/movie_create.html', {'movie_form': movie_form})


# List existing movies
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})


# Delete movie
def movie_delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    messages.success(request, '{}'.format('Película {} eliminada exitosamente'.format(movie.name)))
    return redirect(movie_list)
