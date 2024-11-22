document.addEventListener("DOMContentLoaded", function () {
  const bgParts = [
    document.getElementById('bg-part1'),
    document.getElementById('bg-part2'),
    document.getElementById('bg-part3'),
    document.getElementById('bg-part4')
];

// Функция для перемещения картинок на фоне
function moveBackgroundImages() {
    const scrollPosition = window.scrollY;

    // Двигаем картинки слева и справа
    bgParts.forEach((part, index) => {
        const speed = index % 2 === 0 ? 0.2 : 0.3; // Скорость для разных картинок
        if (index % 2 === 0) {
            part.style.left = -200 + scrollPosition * speed + 'px'; // Перемещаем картинки слева
        } else {
            part.style.right = -200 + scrollPosition * speed + 'px'; // Перемещаем картинки справа
        }
    });
}

// Запускаем движение при прокрутке страницы
window.addEventListener('scroll', moveBackgroundImages);


  // Получаем все изображения деталей
  const parts = document.querySelectorAll("#top img");
  const speed = 2; // Скорость движения картинок
  const maxX = document.body.scrollWidth - 100; // Максимальная горизонтальная позиция (ширина страницы)
  const maxY = document.body.scrollHeight - 100; // Максимальная вертикальная позиция (высота страницы)

  // Начальные координаты и направления для каждой картинки
  const state = Array.from(parts).map(part => ({
      element: part,
      x: Math.random() * maxX, // Начальная позиция по оси X
      y: Math.random() * maxY, // Начальная позиция по оси Y
      dx: (Math.random()) * speed, // Скорость по оси X
      dy: (Math.random()) * speed, // Скорость по оси Y
  }));

  // Функция обновления позиции
  function updatePositions() {
      state.forEach(item => {
          // Обновляем позицию
          item.x += item.dx;
          item.y += item.dy;

          // Проверяем столкновение с краем страницы и меняем направление
          if (item.x <= 0 || item.x >= maxX) {
              item.dx = -item.dx; // Изменяем направление по оси X
          }
          if (item.y <= 0 || item.y >= maxY) {
              item.dy = -item.dy; // Изменяем направление по оси Y
          }

          // Обновляем положение картинки
          item.element.style.left = item.x + "px";
          item.element.style.top = item.y + "px";
      });

      // Повторно вызываем updatePositions на следующем кадре
      requestAnimationFrame(updatePositions);
  }

  // Начинаем обновление
  updatePositions();
});

