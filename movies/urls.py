from django.urls import path

from movies.views import movie_list, movie_detail

urlpatterns = [
    path('list', movie_list, name='movie_list'),
    path('detail/<pk>', movie_detail, name='movie_detail'),
]
