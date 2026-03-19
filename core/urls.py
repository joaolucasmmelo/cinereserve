from django.urls import path
from .views import MovieListView, SessionsPerMovieListView

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:movie_id>/sessions/', SessionsPerMovieListView.as_view(), name='movie-sessions'),
]
