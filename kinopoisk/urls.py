from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    MovieListView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
    MoviesView,
    SeriesView,
    СartoonView,
    MovieDetailView, MovieCarouselView,
)

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),  # Список фильмов

    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),  # Детали фильма
    path('movies/create/', MovieCreateView.as_view(), name='movie_create'),  # Создание фильма
    path('movies/<int:pk>/update/', MovieUpdateView.as_view(), name='movie_update'),  # Обновление фильма
    path('movies/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),  # Удаление фильма

    path('movies/', MoviesView.as_view(), name='movies'),  # Фильмы
    path('series/', SeriesView.as_view(), name='series'),  # Сериалы
    path('сartoon/', СartoonView.as_view(), name='cartoon'),  # Мульфильмы

    path('', MovieCarouselView.as_view(), name='movie_list'),  # Карусель фильмов
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
