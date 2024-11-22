document.addEventListener("DOMContentLoaded", function () {
    const bgParts = [
      document.getElementById('bg-part1'),
      document.getElementById('bg-part2'),
      document.getElementById('bg-part3'),
      document.getElementById('bg-part4')
  ];

  function moveBackgroundImages() {
      const scrollPosition = window.scrollY;

      bgParts.forEach((part, index) => {
          const speed = index % 2 === 0 ? 0.2 : 0.3; 
          if (index % 2 === 0) {
              part.style.left = -200 + scrollPosition * speed + 'px';
          } else {
              part.style.right = -200 + scrollPosition * speed + 'px';
          }
      });
  }


  window.addEventListener('scroll', moveBackgroundImages);


  const parts = document.querySelectorAll("#top img");
  const speed = 2;
  const maxX = document.body.scrollWidth - 100;
  const maxY = document.body.scrollHeight - 100; 

  const state = Array.from(parts).map(part => ({
      element: part,
      x: Math.random() * maxX, 
      y: Math.random() * maxY, 
      dx: (Math.random() - 0.5) * speed,
      dy: (Math.random() - 0.5) * speed,
  }));

  function updatePositions() {
      state.forEach(item => {
        item.x += item.dx;
          item.y += item.dy;
          if (item.x <= 0 || item.x >= maxX) {
              item.dx = -item.dx;
          }
          if (item.y <= 0 || item.y >= maxY) {
              item.dy = -item.dy; 
          }
          item.element.style.left = item.x + "px";
          item.element.style.top = item.y + "px";
      });
      requestAnimationFrame(updatePositions);
  }
    updatePositions();
});

