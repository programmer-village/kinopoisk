from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from .forms import MovieForm
from .models import Genre, Director, Movie, MediaType

from django.views import View

from django.shortcuts import render, redirect


# Проверка является ли пользователь суперпользователем
def superuser_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
    return decorated_view_func


class MovieListView(View):
    def get(self, request):
        genre_name = request.GET.get('genre', 'all')
        search_query = request.GET.get('search', '')
        movies = Movie.objects.all()
        genres = Genre.objects.all()

        if genre_name and genre_name != 'all':
            print(f"Фильтруем по жанру: {genre_name}")
            movies = movies.filter(genre__name=genre_name)  # Фильтрация по имени жанра

        if search_query:
            print(f"Фильтруем по названию: {search_query}")
            movies = movies.filter(title__icontains=search_query)  # Фильтрация по названию фильма

        print(f"Количество фильмов после фильтрации: {movies.count()}")

        return render(request, 'movies/movie_list.html', {
            'movies': movies,
            'genres': genres,
            'selected_genre': genre_name,
            'search_query': search_query
        })


# Получение информации о конкретном фильме
class MovieDetailView(View):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        return render(request, './movies/movie_detail.html', {'movie': movie})


@method_decorator(superuser_required, name='dispatch')
class MovieCreateView(View):
    def get(self, request):
        form = MovieForm()
        return render(request, 'movies/movie_form.html', {
            'form': form,
            'genres': Genre.objects.all(),
            'directors': Director.objects.all(),
            'media_types': MediaType.objects.all(),
        })

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        trailer = request.POST.get('trailer')
        year = request.POST.get('year')
        rating = request.POST.get('rating')
        genre_input = request.POST.get('genre')

        # Зачем-то получаем имя режиссёра вручную
        director_name = request.POST.get('director').strip()
        director, _ = Director.objects.get_or_create(name=director_name)

        # Получаем media_type по ID
        media_type_id = request.POST.get('media_type')
        media_type = MediaType.objects.get(id=media_type_id)

        # Обработка файла изображения
        image = request.FILES.get('image')

        if not all([title, description, trailer, year, rating, genre_input, director_name, media_type_id]):
            return render(request, 'movies/movie_form.html', {
                'error': 'Пожалуйста, заполните все обязательные поля.',
                'form': MovieForm(request.POST, request.FILES),  # Отправляем заполненные значения формы
                'genres': Genre.objects.all(),
                'directors': Director.objects.all(),
                'media_types': MediaType.objects.all(),
            })

        # Получаем или создаем жанр по имени
        genre, _ = Genre.objects.get_or_create(name=genre_input)

        # Создаем экземпляр фильма
        movie = Movie.objects.create(
            title=title,
            description=description,
            trailer=trailer,
            year=year,
            rating=rating,
            genre=genre,
            director=director,
            media_type=media_type,  # Используем объект MediaType
            image=image
        )

        return redirect('movie_detail', pk=movie.pk)


@method_decorator(superuser_required, name='dispatch')
class MovieUpdateView(View):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        genres = Genre.objects.all()
        directors = Director.objects.all()
        media_types = MediaType.objects.all()  # Получаем все доступные типы медиа

        return render(request, './movies/update.html', {
            'movie': movie,
            'genres': genres,
            'directors': directors,
            'media_types': media_types  # Передаем в шаблон
        })

    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.title = request.POST.get('title')
        movie.description = request.POST.get('description')
        movie.trailer = request.POST.get('trailer')
        movie.year = request.POST.get('year')
        movie.rating = request.POST.get('rating')

        genre_id = request.POST.get('genre')
        director_id = request.POST.get('director')
        media_type_id = request.POST.get('media_type')

        genre = get_object_or_404(Genre, id=genre_id)
        director = get_object_or_404(Director, id=director_id)
        media_type = get_object_or_404(MediaType, id=media_type_id)

        movie.genre = genre
        movie.director = director
        movie.media_type = media_type
        movie.save()

        return redirect('movie_detail', pk=movie.pk)


# Удаление фильма
@method_decorator(superuser_required, name='dispatch')
class MovieDeleteView(View):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        return render(request, './movies/movie_confirm_delete.html', {'movie': movie})

    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return redirect('movie_list')


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.filter(media_type_id=1)

        return render(request, './menu/movies.html', {
            'movies': movies,
        })


class SeriesView(View):
    def get(self, request):
        movies = Movie.objects.filter(media_type_id=2)
        return render(request, './menu/series.html', {
            'movies': movies,
        })


class СartoonView(View):
    def get(self, request):
        movies = Movie.objects.filter(media_type_id=3)
        return render(request, './menu/cartoon.html', {
            'movies': movies,
        })


class MovieCarouselView(View):
    def get(self, request):
        movies = Movie.objects.all()  # Получаем все фильмы из базы данных
        return render(request, './movies/movie_list.html', {
            'movies': movies
        })
