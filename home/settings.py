"""
Настройки Django для проекта home.

Сгенерировано командой 'django-admin startproject' с использованием Django 5.1.

Дополнительную информацию можно найти в
https://docs.djangoproject.com/en/5.1/topics/settings/

Полный список настроек и их значений можно увидеть в
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

# Построение путей внутри проекта, например: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ВНИМАНИЕ БЕЗОПАСНОСТИ: храните секретный ключ в секрете для продакшн-версии!
SECRET_KEY = 'django-insecure-y_g$n8b*%(qqi4afl02)8xin+-)=gt^6gttbe6e2jur_1v44@b'

# ВНИМАНИЕ БЕЗОПАСНОСТИ: не запускайте с включенным отладкой в продакшн-версии!
DEBUG = True

# Укажите разрешенные хосты. Замените "*" на конкретные хосты в продакшне.
ALLOWED_HOSTS = ["*"]

# Определение приложений
INSTALLED_APPS = [
    'django.contrib.admin',  # Приложение администрирования Django
    'django.contrib.auth',  # Аутентификация пользователей
    'django.contrib.contenttypes',  # Типы содержимого для общих отношений
    'django.contrib.sessions',  # Управление сессиями
    'django.contrib.messages',  # Фреймворк сообщений
    'django.contrib.staticfiles',  # Управление статическими файлами
    'django.contrib.sites',  # Поддержка нескольких сайтов
    'kinopoisk.apps.KinopoiskConfig',  # Ваше приложение
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Защитное промежуточное ПО
    'django.contrib.sessions.middleware.SessionMiddleware',  # Промежуточное ПО для сессий
    'django.middleware.common.CommonMiddleware',  # Общее промежуточное ПО для различных целей
    'django.middleware.csrf.CsrfViewMiddleware',  # Защита от подделки межсайтовых запросов
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Промежуточное ПО аутентификации
    'django.contrib.messages.middleware.MessageMiddleware',  # Функциональность сообщений
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Защита от кликджакинга
]

ROOT_URLCONF = 'home.urls'  # Основной модуль конфигурации URL

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Использование системы шаблонов Django
        'DIRS': [],  # Дополнительные директории для поиска шаблонов
        'APP_DIRS': True,  # Проверять наличие шаблонов в каталогах приложений
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'home.wsgi.application'  # Точка входа WSGI приложения

# Конфигурация базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Бэкенд базы данных (SQLite)
        'NAME': BASE_DIR / 'db.sqlite3',  # Путь к файлу базы данных
    }
}

# Настройки валидации паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Настройки интернационализации
LANGUAGE_CODE = 'ru'  # Код языка для перевода
TIME_ZONE = 'UTC'  # Часовой пояс приложения
USE_I18N = True  # Включить интернационализацию
USE_TZ = True  # Включить поддержку часовых поясов
# Статические файлы (CSS, JavaScript, изображения)
STATIC_URL = '/static/'  # URL-префикс для статических файлов
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "kinopoisk/static"),  # Путь к директории со статическими файлами
]  # Директория, где находятся статические файлы
MEDIA_URL = '/media/'  # URL-префикс для медиафайлов
MEDIA_ROOT = os.path.join(BASE_DIR, 'kinopoisk/static/kinopoisk/media/movies')  # Директория для загруженных медиафайлов

# URL для переадресации при аутентификации
LOGIN_URL = '/accounts/login/'  # URL для страницы входа
LOGIN_REDIRECT_URL = '/movies/'  # URL, на который перенаправляет после успешного входа

# Тип поля первичного ключа по умолчанию
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Тип поля первичного ключа
# settings.py
SITE_ID = 1
