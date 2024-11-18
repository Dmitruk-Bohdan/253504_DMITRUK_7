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
  let slideInterval;
  let delay = 3000;
  let loop = true;

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
    
    const currentSlide = slides[displayIndex - 1];
    const text = currentSlide.getAttribute('data-text');
    slideText.textContent = text;
  };

  // Слушатели событий для кнопок
  prevButton.addEventListener('click', () => {
    if(loop)
    {
      slideIndex--;
      slide();
      if (slideIndex < 1) {
        setTimeout(() => {
          slider.style.transition = 'none';
          slideIndex = slideCount; // Переход к последнему реальному слайду
          slider.style.transform = `translateX(${-slideIndex * imageWidth}px)`;
        }, 500);
      }
    }
    else{
      if(slideIndex > 1)
      {
        slideIndex--;
        slide();
      }
    }
   
  });

  nextButton.addEventListener('click', () => {
    if(loop)
    {
      slideIndex++;
      slide();
      if (slideIndex > slideCount) {
        setTimeout(() => {
          slider.style.transition = 'none';
          slideIndex = 1; // Переход к первому реальному слайду
          slider.style.transform = `translateX(${-imageWidth}px)`;
        }, 500);
      }
    }
    else{
      if(slideIndex < (slideCount))
      {
        slideIndex++;
        slide();
      }
    }
  });

  // Автоматическая прокрутка слайдов
  const autoSlide = () => {
    if(loop)
      {
        slideIndex++;
        slide();
        if (slideIndex > slideCount) {
          setTimeout(() => {
            slider.style.transition = 'none';
            slideIndex = 1; // Переход к первому реальному слайду
            slider.style.transform = `translateX(${-imageWidth}px)`;
          }, 500);
        }
      }
      else{
        if(slideIndex < (slideCount))
        {
          slideIndex++;
          slide();
        }
      }
  };

  const startAutoSlide = (delay) => {
    // Остановить текущий интервал, если он был
    if (slideInterval) {
      clearInterval(slideInterval);
    }
    
    // Устанавливаем новый интервал
    slideInterval = setInterval(autoSlide, delay);
  };

  const stopAutoSlide = () => {
    clearInterval(slideInterval);
  };
  
  // Инициализация слайдера после загрузки
  window.addEventListener('load', () => {
    slide();
    startAutoSlide(delay); 
  });

  document.getElementById('slider-settings-form').addEventListener('submit', (e) => {
    e.preventDefault();
  
    const loopAvailable = document.getElementById('loop').checked;
    const navs = document.getElementById('navs').checked;
    const pags = document.getElementById('pags').checked;
    const isAuto = document.getElementById('auto').checked;
    const stopOnHover = document.getElementById('stopMouseHover').checked;
    const delayValue = document.getElementById('delay').value;
    const delay = delayValue && !isNaN(delayValue) ? parseInt(delayValue) * 1000 : 5000;

    loop = loopAvailable

    if (navs) {
      enableButtons();
    } else {
      disableButtons();
    }

    if (pags) {
      enablePagination();
    } else {
      disablePagination();
    }

    if (isAuto) {
      startAutoSlide(delay);  // Перезапуск с новым интервалом
    } else {
      stopAutoSlide();  // Остановка автопереключения
    }

    if (stopOnHover) {
      slider.addEventListener('mouseenter', stopAutoSlide);
      slider.addEventListener('mouseleave', () => startAutoSlide(delay));
    }

  });
  
  function disableButtons() {
    const buttons = document.querySelectorAll('.prev-button, .next-button');
    buttons.forEach(button => {
      button.style.visibility = 'hidden';
      button.style.pointerEvents = 'none';
    });
  }
  
  function enableButtons() {
    const buttons = document.querySelectorAll('.prev-button, .next-button');
    buttons.forEach(button => {
      button.style.visibility = 'visible';
      button.style.pointerEvents = 'auto';
    });
  }
  
  function disablePagination() {
    const indicators = document.querySelectorAll('.indicators .indicator');
    indicators.forEach(indicator => {
      indicator.style.visibility = 'hidden';
      indicator.style.pointerEvents = 'none';
    });
  }
  
  function enablePagination() {
    const indicators = document.querySelectorAll('.indicators .indicator');
    indicators.forEach(indicator => {
      indicator.style.visibility = 'visible';
      indicator.style.pointerEvents = 'auto';
    });
  }  

});
