import json
from django.core.management.base import BaseCommand
from kinopoisk.models import Genre, Director, Movie, MediaType


class Command(BaseCommand):
    help = 'Загружает фильмы, жанры и режиссёров из JSON файлов'

    def handle(self, *args, **kwargs):
        # Загрузка жанров
        with open('kinopoisk_json/genre.json', 'r', encoding='utf-8') as genre_file:
            genres = json.load(genre_file)
            for genre_data in genres:
                genre, created = Genre.objects.get_or_create(name=genre_data['name'])
                if created:
                    self.stdout.write(self.style.SUCCESS('Жанр "%s" был создан.' % genre.name))

        with open('kinopoisk_json/mediatype.json', 'r', encoding='utf-8') as media_file:
            media_type = json.load(media_file)
            for media_data in media_type:
                media, created = MediaType.objects.get_or_create(name=media_data['name'])
                if created:
                    self.stdout.write(self.style.SUCCESS('Media "%s" был создан.' % media.name))

        # Загрузка режиссёров
        with open('kinopoisk_json/director.json', 'r', encoding='utf-8') as director_file:
            directors = json.load(director_file)
            for director_data in directors:
                director, created = Director.objects.get_or_create(name=director_data['name'])
                if created:
                    self.stdout.write(self.style.SUCCESS('Режиссёр "%s" был создан.' % director.name))

        # Загрузка фильмов
        with open('kinopoisk_json/movie.json', 'r', encoding='utf-8') as movie_file:
            movies = json.load(movie_file)
            for movie_data in movies:
                genre = Genre.objects.get(id=movie_data['genre_id'])
                director = Director.objects.get(id=movie_data['director_id'])
                media_type = MediaType.objects.get(id=movie_data['media_type_id'])
                movie = Movie(
                    title=movie_data['title'],
                    description=movie_data['description'],
                    trailer=movie_data['trailer'],
                    year=movie_data['year'],
                    rating=movie_data['rating'],
                    media_type=media_type,
                    genre=genre,
                    director=director,
                    external_image_url=movie_data['external_image_url']
                )
                movie.save()
                self.stdout.write(self.style.SUCCESS('Фильм "%s" был создан.' % movie.title))
