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


    const addEmployeeBtn = document.getElementById("add-employee-btn");
    const addEmployeeForm = document.getElementById("add-employee-form");
    const employeeForm = document.getElementById("employee-form");
    const validationMessage = document.getElementById("validation-message");

      // Показать или скрыть форму добавления
  addEmployeeBtn.addEventListener("click", function () {
    addEmployeeForm.style.display = addEmployeeForm.style.display === "none" ? "block" : "none";
  });

  // Функция для валидации URL
  function validateURL(url) {
    const regex = /^(http:\/\/|https:\/\/).*\.(php|html)$/;
    return regex.test(url);
  }

  // Функция для валидации телефона
  function validatePhone(phone) {
    const regex = /^(\+375|8)\s*\(?\d{2}\)?\s*\d{3}[- ]?\d{2}[- ]?\d{2}$/;
    return regex.test(phone);
  }

  // Обработчик отправки формы
  employeeForm.addEventListener("submit", function (e) {
    e.preventDefault();

    // Получаем значения полей
    const fullName = document.getElementById("full-name").value;
    const jobDesc = document.getElementById("job-desc").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
    const url = document.getElementById("url").value;
    const photo = document.getElementById("photo").files[0];

    // Выполняем валидацию
    if (!validateURL(url)) {
      validationMessage.textContent = "Неверный формат URL.";
      document.getElementById("url").style.border = "2px solid red";
      document.getElementById("url").style.backgroundColor = "pink";
      return;
    }

    if (!validatePhone(phone)) {
      validationMessage.textContent = "Неверный формат номера телефона.";
      document.getElementById("phone").style.border = "2px solid red";
      document.getElementById("phone").style.backgroundColor = "pink";
      return;
    }

    // Если валидация пройдена
    validationMessage.textContent = "";
    document.getElementById("url").style.border = "";
    document.getElementById("url").style.backgroundColor = "";
    document.getElementById("phone").style.border = "";
    document.getElementById("phone").style.backgroundColor = "";

    // Создаем новую строку для таблицы
    const newRow = document.createElement("tr");
    newRow.classList.add("employee-row");
    newRow.setAttribute("data-included", "on");

    // Добавляем ячейки с данными
    newRow.innerHTML = `
      <td><img src="${URL.createObjectURL(photo)}" alt="Photo" class="employee-img" style="width: 50px; height: 50px;"/></td>
      <td>${fullName}</td>
      <td>${jobDesc}</td>
      <td>${email}</td>
      <td>${phone}</td>
      <td>${url}</td>
      <td><input type="checkbox" name="employee_select"></td>
    `;

    // Добавляем новую строку в таблицу
    document.querySelector(".employee-table tbody").appendChild(newRow);

    // Сбрасываем форму и скрываем её
    employeeForm.reset();
    addEmployeeForm.style.display = "none";

    // Обновляем пагинацию и показываем первую страницу
    rows = Array.from(document.querySelectorAll(".employee-row")); // Обновляем массив строк
    currentPage = 1;
    showPage(currentPage);
    updatePagination();
  });
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
  
  function toggleDetails(row) {
    // Находим блок с деталями сотрудника
    var detailsDiv = document.getElementById('employee-details');
    
    // Проверяем, отображается ли блок
    if (detailsDiv.style.display === 'block') {
        // Если блок уже отображается, скрываем его
        detailsDiv.style.display = 'none';
    } else {
        // Если блок не отображается, показываем его и обновляем содержимое
        var cells = row.getElementsByTagName('td');
        
        var photo = cells[0].querySelector('img').src;  // Фото
        var name = cells[1].innerText;  // Имя (first_name + last_name)
        var jobDescription = cells[2].innerText;  // Описание работы
        var email = cells[3].innerText;  // Email
        var phoneNumber = cells[4].innerText;  // Номер телефона
        var profileUrl = cells[5].innerText;  // URL профиля

        detailsDiv.innerHTML = `
            <h3>Детали сотрудника</h3>
            <p>Фото: <img src="${photo}" alt="Employee Photo" style="width: 100px; height: 100px;"></p>
            <p>Имя: ${name}</p>
            <p>Описание работы: ${jobDescription}</p>
            <p>Email: ${email}</p>
            <p>Номер телефона: ${phoneNumber}</p>
            <p>URL профиля: ${profileUrl}</p>
        `;

        detailsDiv.style.display = 'block';
    }
}
