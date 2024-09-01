const carouselWrapper = document.querySelector('.carousel-wrapper');

carouselWrapper.addEventListener('mouseover', () => {
    carouselWrapper.style.animationPlayState = 'paused';
});

carouselWrapper.addEventListener('mouseout', () => {
    carouselWrapper.style.animationPlayState = 'running';
});

function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth' // Добавляет плавную прокрутку
    });
}

// Показать/скрыть кнопку в зависимости от прокрутки
window.onscroll = function () {
    const button = document.querySelector('.scroll-to-top');
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
};
