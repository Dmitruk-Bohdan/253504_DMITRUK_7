document.addEventListener("DOMContentLoaded", function() {
    const rowsPerPage = 3;  // Количество строк на одной странице
    let rows = Array.from(document.querySelectorAll('.employee-row')); // Все строки сотрудников
    let currentPage = 1;  // Текущая страница

    // Функция для показа только тех строк, которые относятся к текущей странице
    function showPage(page) {
        const filteredRows = rows.filter(row => row.getAttribute('data-included') === 'on'); // Фильтрация строк по атрибуту data-included

        // Скрываем все строки
        rows.forEach(row => row.style.display = 'none');
        
        // Показываем только те строки, которые должны быть на текущей странице
        filteredRows.forEach((row, index) => {
            const start = (page - 1) * rowsPerPage;
            const end = page * rowsPerPage;
            row.style.display = (index >= start && index < end) ? '' : 'none';
        });
    }

    // Функция для обновления кнопок пагинации
    function updatePagination() {
        const paginationElement = document.getElementById('pagination');
        paginationElement.innerHTML = '';  // Очищаем пагинацию

        const filteredRows = rows.filter(row => row.getAttribute('data-included') === 'on');
        const totalPages = Math.ceil(filteredRows.length / rowsPerPage);  // Количество страниц для отфильтрованных строк

        // Кнопка "Назад"
        const prevButton = document.createElement('button');
        prevButton.textContent = 'Назад';
        prevButton.disabled = currentPage === 1;
        prevButton.onclick = function() {
            if (currentPage > 1) {
                currentPage--;
                showPage(currentPage);
                updatePagination();
            }
        };
        paginationElement.appendChild(prevButton);

        // Кнопки с номерами страниц
        for (let i = 1; i <= totalPages; i++) {
            const pageButton = document.createElement('button');
            pageButton.textContent = i;
            pageButton.classList.toggle('active', i === currentPage);
            pageButton.onclick = function() {
                currentPage = i;
                showPage(currentPage);
                updatePagination();
            };
            paginationElement.appendChild(pageButton);
        }

        // Кнопка "Вперед"
        const nextButton = document.createElement('button');
        nextButton.textContent = 'Вперед';
        nextButton.disabled = currentPage === totalPages;
        nextButton.onclick = function() {
            if (currentPage < totalPages) {
                currentPage++;
                showPage(currentPage);
                updatePagination();
            }
        };
        paginationElement.appendChild(nextButton);
    }

    // Функция фильтрации строк по введённому значению
    function filterRows(searchText) {
        rows.forEach(row => {
            let isMatch = false;
            // Получаем все текстовые значения в строке
            row.querySelectorAll('td').forEach(cell => {
                if (cell.innerText.toLowerCase().includes(searchText.toLowerCase())) {
                    isMatch = true;
                }
            });

            // Если совпадение найдено, ставим data-included="on", иначе - "off"
            row.setAttribute('data-included', isMatch ? 'on' : 'off');
        });

        // После фильтрации показываем первую страницу
        currentPage = 1;
        showPage(currentPage);
        updatePagination();
    }

    // Обработчик поиска по кнопке
    const searchButton = document.getElementById('search-button');
    const searchInput = document.getElementById('search-input');
    searchButton.addEventListener('click', function() {
        const searchText = searchInput.value;
        filterRows(searchText);  // Запуск фильтрации
    });

    // Изначально показываем первую страницу
    showPage(currentPage);
    updatePagination();
});


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
  