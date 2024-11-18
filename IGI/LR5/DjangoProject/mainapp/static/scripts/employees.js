function sortTable(columnIndex) {
    const table = document.querySelector('.employee-table');
    const rows = Array.from(table.querySelectorAll('tbody tr'));
    
    // Получаем направление сортировки: по умолчанию сортируем по возрастанию
    const isAscending = table.querySelectorAll('th')[columnIndex].classList.contains('ascending');
    
    // Сортировка строк по столбцу
    rows.sort((rowA, rowB) => {
      const cellA = rowA.cells[columnIndex].innerText.trim().toLowerCase();
      const cellB = rowB.cells[columnIndex].innerText.trim().toLowerCase();
  
      // Сортировка строк в зависимости от типа данных (числа или текст)
      if (!isNaN(cellA) && !isNaN(cellB)) {
        return parseFloat(cellA) - parseFloat(cellB); // Числовая сортировка
      } else {
        return cellA.localeCompare(cellB); // Сортировка по тексту
      }
    });
  
    // Добавляем строки обратно в таблицу
    rows.forEach(row => table.querySelector('tbody').appendChild(row));
  
    // Меняем направление сортировки
    table.querySelectorAll('th').forEach(th => th.classList.remove('ascending', 'descending'));
    if (isAscending) {
      table.querySelectorAll('th')[columnIndex].classList.add('descending');
    } else {
      table.querySelectorAll('th')[columnIndex].classList.add('ascending');
    }
  }
  