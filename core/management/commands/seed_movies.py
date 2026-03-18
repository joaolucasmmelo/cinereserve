from django.core.management.base import BaseCommand
from core.models import Movie
import random


class Command(BaseCommand):
    help = 'Seeds the database with 100 random movies'

    def handle(self, *args, **kwargs):
        adjectives = ["The Last", "Incredible", "Golden", "Silent",
                      "Fast", "Shadow", "Infinite", "Ancient", "Dark", "Star"]
        nouns = ["Journey", "War", "Kingdom", "Night", "Walker", "City", "Ocean", "Memory", "Legend", "Prophecy"]
        genres = ["Action", "Drama", "Sci-Fi", "Comedy", "Horror",
                  "Thriller", "Adventure", "Fantasy", "Mystery", "Romance"]

        movies = []
        for i in range(100):
            name = f"{random.choice(adjectives)} {random.choice(nouns)} {i+1}"
            description = f"A {random.choice(genres)} movie about {random.choice(adjectives).lower()} {random.choice(nouns).lower()}."
            duration_minutes = random.randint(80, 180)

            movies.append(Movie(
                name=name,
                description=description,
                duration_minutes=duration_minutes
            ))

        Movie.objects.bulk_create(movies)
        self.stdout.write(self.style.SUCCESS('Successfully seeded 100 movies'))
