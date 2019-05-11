from django.urls import path

from movies.views import movie_list, movie_detail, movie_create, movie_delete

urlpatterns = [
    path('create', movie_create, name='movie_create'),
    path('list', movie_list, name='movie_list'),
    path('detail/<pk>', movie_detail, name='movie_detail'),
    path('delete/<pk>', movie_delete, name='movie_delete'),
]
