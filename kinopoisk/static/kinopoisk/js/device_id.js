// Функция для генерации уникального ID
function generateDeviceId() {
    return 'device-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9);
}

// Получаем и устанавливаем deviceId в localStorage
const deviceId = localStorage.getItem('device_id') || generateDeviceId();
localStorage.setItem('device_id', deviceId);

// Обработчик отправки формы регистрации
document.getElementById('registrationForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Отменяем стандартную отправку формы

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const registrationData = {
        username: username,
        password: password,
        device_id: deviceId,
    };

    // Отправка данных на сервер с помощью fetch или XMLHttpRequest
    fetch('/register/', { // Укажите правильный URL для регистрации
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'), // Убедитесь, что CSRF-токен передан
        },
        body: JSON.stringify(registrationData),
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = '/movie_list/'; // Перенаправление на нужную страницу
            } else {
                console.error(data.error);
            }
        })
        .catch((error) => {
            console.error('Ошибка:', error);
        });
});

// Функция для получения CSRF-токена
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Смотрим, начинается ли этот cookie с нужного имени
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}