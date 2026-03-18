from .models import Movie, Session
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'duration_minutes']


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['session_id', 'datetime']
