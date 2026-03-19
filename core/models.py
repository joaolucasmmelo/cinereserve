from django.db import models

# # Create your models here.


class Movie(models.Model):
    name: str = models.CharField(max_length=128)
    description: str = models.TextField()
    duration_minutes: int = models.IntegerField()


class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField(default=16)


class Session(models.Model):
    movie: Movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='sessions')
    room: Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __str__(self):
        return f"Sessão para o filme: {self.movie.name}, na {self.room.name} as {self.datetime}"
