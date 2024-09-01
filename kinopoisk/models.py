from django.db import models
from django.contrib.auth.models import AbstractUser


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Жанр')

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name='Режиссёр')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Режиссёр'
        verbose_name_plural = 'Режиссёры'


class MediaType(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тип медиа')

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название фильма')
    description = models.TextField(verbose_name='Описание фильма')
    trailer = models.URLField(verbose_name='Ссылка на трейлер')
    year = models.IntegerField(verbose_name='Год выхода')
    rating = models.CharField(max_length=5, verbose_name='Рейтинг')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name='Режиссёр')
    image = models.ImageField(upload_to='movies/', verbose_name='Изображение', blank=True, null=True)
    external_image_url = models.URLField(blank=True, null=True)

    # Связь с моделью MediaType
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE, verbose_name='Тип медиа', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
