from django.urls import path

from movies.views import movie_list, movie_create_or_edit, movie_delete

urlpatterns = [
    path('create', movie_create_or_edit, name='movie_create'),
    path('edit/<pk>', movie_create_or_edit, name='movie_edit'),
    path('list', movie_list, name='movie_list'),
    path('delete/<pk>', movie_delete, name='movie_delete'),
]
