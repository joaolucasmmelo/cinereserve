from django.db import models

# # Create your models here.


class Movie(models.Model):
    name: str = models.CharField(max_length=128)
    description: str = models.TextField()
    duration_minutes: int = models.IntegerField()


class Session(models.Model):
    session_id = models.IntegerField()
    datetime = models.DateTimeField()
