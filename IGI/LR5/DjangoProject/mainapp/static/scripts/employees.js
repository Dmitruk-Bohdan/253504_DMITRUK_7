// Функция для сортировки таблицы
function sortTable(columnIndex) {
    // Получаем таблицу и строки таблицы
    const table = document.querySelector('.employee-table');
    const rows = Array.from(table.querySelectorAll('tbody tr'));
  
    // Определяем порядок сортировки: если у заголовка есть класс 'ascending', то сортируем по убыванию
    const isAscending = table.querySelectorAll('th')[columnIndex].classList.contains('ascending');
  
    // Убираем все классы 'ascending' и 'descending' с всех заголовков
    table.querySelectorAll('th').forEach(th => th.classList.remove('ascending', 'descending'));
  
    // Если текущий порядок был по возрастанию, сортируем по убыванию
    if (isAscending) {
      table.querySelectorAll('th')[columnIndex].classList.add('descending');
    } else {
      table.querySelectorAll('th')[columnIndex].classList.add('ascending');
    }
  
    // Сортируем строки в зависимости от выбранного столбца
    rows.sort((rowA, rowB) => {
      const cellA = rowA.cells[columnIndex].innerText.trim();
      const cellB = rowB.cells[columnIndex].innerText.trim();
  
      // Сортируем строки по возрастанию или убыванию в зависимости от isAscending
      if (isAscending) {
        return cellA > cellB ? -1 : 1; // По убыванию
      } else {
        return cellA < cellB ? -1 : 1; // По возрастанию
      }
    });
  
    // Вставляем отсортированные строки обратно в таблицу
    rows.forEach(row => table.querySelector('tbody').appendChild(row));
  }
  