document.addEventListener('DOMContentLoaded', () => {
    console.log('Скрипт начал выполнение');
    const slider = document.querySelector('.slider');
    const prevButton = document.querySelector('.prev-button');
    const nextButton = document.querySelector('.next-button');
    const slides = Array.from(slider.querySelectorAll('img'));
    const slideCount = slides.length;
    let slideIndex = 0;
  
    prevButton.addEventListener('click', () => {
        alert('Скрипт начал выполнение');
      slideIndex = (slideIndex - 1 + slideCount) % slideCount;
      slide();
    });
  
    nextButton.addEventListener('click', () => {
      slideIndex = (slideIndex + 1) % slideCount;
      slide();
    });
  
    const slide = () => {
      const imageWidth = slider.clientWidth;
      const slideOffset = -slideIndex * imageWidth;
      slider.style.transform = `translateX(${slideOffset}px)`;
    }
  
    // Если нужно подождать загрузки всех изображений
    window.addEventListener('load', () => {
      slide();
    });
  });
  