let movieToDelete;

// Фильтр фильмов
document.getElementById('movieFilter').addEventListener('keyup', function () {
    const filter = this.value.toLowerCase();
    const movies = document.querySelectorAll('#movieList .list-group-item');

    movies.forEach(function (movie) {
        const text = movie.textContent.toLowerCase();
        movie.style.display = text.includes(filter) ? '' : 'none';
    });
});

// Модальное окно для подтверждения удаления
function showDeleteModal(button) {
    movieToDelete = button.closest('.list-group-item'); // Сохраняем ссылку на элемент для удаления
    var myModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    myModal.show();
}

document.getElementById('confirmDelete').addEventListener('click', function () {
    if (movieToDelete) {
        movieToDelete.remove(); // Удаляем элемент из списка
        console.log('Фильм удалён'); // Выводим в консоль для отладки
        movieToDelete = null; // Обнуляем ссылку
    }
});
document.addEventListener('DOMContentLoaded', function () {
    const movieList = document.getElementById('movieList');
    const listItems = movieList.getElementsByTagName('li');

    // Функция для проверки, виден ли последний элемент
    function isLastItemVisible() {
        const lastItem = listItems[listItems.length - 1];
        const rect = lastItem.getBoundingClientRect();
        return rect.bottom <= window.innerHeight;
    }

    // Прокрутка к последнему элементу, если он не виден
    function scrollToLastItemIfNotVisible() {
        if (!isLastItemVisible()) {
            const lastItem = listItems[listItems.length - 1];
            lastItem.scrollIntoView({behavior: 'smooth'});
        }
    }

    // Добавляем обработчик события на scroll
    window.addEventListener('scroll', scrollToLastItemIfNotVisible);

    // Вызываем функцию, чтобы проверить видимость при загрузке
    scrollToLastItemIfNotVisible();
});
