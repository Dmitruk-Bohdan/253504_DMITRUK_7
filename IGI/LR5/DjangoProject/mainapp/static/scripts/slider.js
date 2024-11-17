//бесконечная прокрутка за счет того что дублированы первый и последний слайды и сначала выполняется плавный переход на наих а потом мгновенный на оригинальный слайд

document.addEventListener('DOMContentLoaded', () => {
  console.log('Скрипт начал выполнение');
  const slider = document.querySelector('.slider');
  const prevButton = document.querySelector('.prev-button');
  const nextButton = document.querySelector('.next-button');
  const slides = Array.from(slider.querySelectorAll('img'));
  const indicators = Array.from(document.querySelectorAll('.indicator')); // Индикаторы
  const slideCount = slides.length;
  const slideCounter = document.querySelector('.slide-counter');
  const slideText = document.querySelector('.slide-text'); // Элемент для текста
  let slideIndex = 1; // Начинаем с 1, чтобы учесть клонированный слайд

  // Клонируем первый и последний слайды
  const firstClone = slides[0].cloneNode(true);
  const lastClone = slides[slideCount - 1].cloneNode(true);

  // Добавляем клоны в DOM
  slider.appendChild(firstClone);
  slider.insertBefore(lastClone, slides[0]);

  const imageWidth = slider.clientWidth;
  slider.style.transform = `translateX(${-imageWidth}px)`;

  // Функция для смены слайда
  const slide = () => {
    slider.style.transition = 'transform 0.5s ease-in-out';
    const slideOffset = -slideIndex * imageWidth;
    slider.style.transform = `translateX(${slideOffset}px)`;

    // Обновление активного индикатора
    indicators.forEach((indicator, index) => {
      if (index === (slideIndex - 1 + slideCount) % slideCount) {
        indicator.classList.add('active');
      } else {
        indicator.classList.remove('active');
      }
    });

    let displayIndex = (slideIndex - 1 + slideCount) % slideCount + 1;
    slideCounter.textContent = `${displayIndex}/${slideCount}`;

    const currentSlide = slides[slideIndex];
    const text = currentSlide.getAttribute('data-text');
    slideText.textContent = text;
  };

  slides.forEach(slide => {
    slide.addEventListener('click', () => {
      const href = slide.getAttribute('data-href');
      if (href) {
        window.location.href = href; // Переход на URL
      }
    });
  });

  // Слушатели событий для кнопок
  prevButton.addEventListener('click', () => {
    slideIndex--;
    slide();
    if (slideIndex < 1) {
      setTimeout(() => {
        slider.style.transition = 'none';
        slideIndex = slideCount; // Переход к последнему реальному слайду
        slider.style.transform = `translateX(${-slideIndex * imageWidth}px)`;
      }, 500);
    }
  });

  nextButton.addEventListener('click', () => {
    slideIndex++;
    slide();
    if (slideIndex > slideCount) {
      setTimeout(() => {
        slider.style.transition = 'none';
        slideIndex = 1; // Переход к первому реальному слайду
        slider.style.transform = `translateX(${-imageWidth}px)`;
      }, 500);
    }
  });

  // Автоматическая прокрутка слайдов
  const autoSlide = () => {
    slideIndex++;
    slide();
    if (slideIndex > slideCount) {
      setTimeout(() => {
        slider.style.transition = 'none';
        slideIndex = 1;
        slider.style.transform = `translateX(${-imageWidth}px)`;
      }, 500);
    }
  };

  let slideInterval = setInterval(autoSlide, 3000);

  // Добавление событий для клика на индикатор
  indicators.forEach((indicator, index) => {
    indicator.addEventListener('click', () => {
      slideIndex = index + 1; // +1, чтобы учесть клонированный слайд
      slide();
    });
  });

  // Инициализация слайдера после загрузки
  window.addEventListener('load', () => {
    slide();
  });
});
