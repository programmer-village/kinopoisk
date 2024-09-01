document.addEventListener('DOMContentLoaded', () => {
    const navbarNav = document.getElementById('navbarNav');
    const popupMenu = document.getElementById('popupMenu');

    // Установка начальной видимости меню в заголовке
    navbarNav.style.display = window.innerWidth > 700 ? 'flex' : 'none'; // Изначально видно или скрыто
    popupMenu.style.display = 'none'; // Начально скрыто

    // Функция для переключения меню
    window.toggleMenu = function() {
        if (popupMenu.style.display === 'block') {
            popupMenu.style.display = 'none'; // Скрываем всплывающее меню
            navbarNav.style.display = 'flex'; // Показываем меню в заголовке
        } else {
            popupMenu.style.display = 'block'; // Показываем всплывающее меню
            navbarNav.style.display = 'none'; // Скрываем меню в заголовке
        }
    };

    // Обработчик изменения размера окна
    window.addEventListener('resize', () => {
        if (window.innerWidth > 700) {
            navbarNav.style.display = 'flex'; // Показываем меню в заголовке
            popupMenu.style.display = 'none'; // Скрываем всплывающее меню
        } else {
            navbarNav.style.display = 'none'; // Скрываем меню в заголовке
        }
    });
});