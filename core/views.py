from rest_framework import generics
from .models import Movie, Session
from .serializers import MovieSerializer, SessionSerializer


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SessionsPerMovieListView(generics.ListAPIView):
    serializer_class = SessionSerializer

    def get_queryset(self):
        return Session.objects.filter(movie_id=self.kwargs['movie_id'])
