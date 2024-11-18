console.log("Employee List JS Loaded");

document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM fully loaded and parsed");

  const apiUrl = "/webpages/api/contacts/"; // Обновленный URL API
  let contacts = [];
  let currentPage = 1;
  const itemsPerPage = 3;
  let currentSort = { column: null, direction: "asc" };
  let filteredContacts = [];
  let selectedEmployees = [];

  const employeeTableBody = document.querySelector("#employee-table tbody");
  const currentPageSpan = document.getElementById("current-page");
  const totalPagesSpan = document.getElementById("total-pages");
  const prevPageBtn = document.getElementById("prev-page");
  const nextPageBtn = document.getElementById("next-page");
  const filterBtn = document.getElementById("filter-btn");
  const filterInput = document.getElementById("filter-input");
  const employeeDetails = document.getElementById("employee-details");
  const addEmployeeBtn = document.getElementById("add-employee-btn");
  const addEmployeeModal = document.getElementById("add-employee-modal");
  const modalClose = document.getElementById("modal-close");
  const addEmployeeForm = document.getElementById("add-employee-form");
  const submitEmployeeBtn = document.getElementById("submit-employee-btn");
  const formResult = document.getElementById("form-result");
  const photoUrlInput = document.getElementById("photo_url");
  const phoneInput = document.getElementById("phone");
  const photoUrlError = document.getElementById("photo_url_error");
  const phoneError = document.getElementById("phone_error");
  const awardBtn = document.getElementById("award-btn");
  const awardText = document.getElementById("award-text");

  // Получение остальных полей формы
  const fullNameInput = document.getElementById("full_name");
  const jobDescriptionInput = document.getElementById("job_description");
  const emailInput = document.getElementById("email");

  // Проверка элементов
  console.log(addEmployeeBtn, addEmployeeModal, modalClose);

  // Функция для загрузки данных с сервера
  async function loadContacts() {
    try {
      const response = await fetch(apiUrl);
      if (!response.ok) {
        throw new Error(`Ошибка ${response.status}: ${response.statusText}`);
      }
      contacts = await response.json();
      filteredContacts = contacts.slice();
      renderTable();
      renderPagination();
      console.log("Contacts loaded successfully");
    } catch (error) {
      console.error("Ошибка при загрузке данных:", error);
      employeeTableBody.innerHTML = `<tr><td colspan="6">Не удалось загрузить данные.</td></tr>`;
    }
    // Удалено: preloader.classList.add("hidden");
  }

  function renderTable() {
    employeeTableBody.innerHTML = "";
    const start = (currentPage - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    const paginatedContacts = filteredContacts.slice(start, end);

    if (paginatedContacts.length === 0) {
      employeeTableBody.innerHTML = `<tr><td colspan="6">Нет сотрудников для отображения.</td></tr>`;
      return;
    }

    paginatedContacts.forEach((contact) => {
      const row = document.createElement("tr");
      row.dataset.id = contact.id;

      const isChecked = selectedEmployees.includes(contact.id); // Проверяем, выбран ли сотрудник

      row.innerHTML = `
      <td>${contact.full_name}</td>
      <td><img src="${contact.photo_url}" alt="Фото"></td>
      <td>${contact.job_description}</td>
      <td>${contact.phone}</td>
      <td>${contact.email}</td>
      <td><input type="checkbox" class="select-checkbox" value="${contact.id}" ${
        isChecked ? "checked" : ""
      }></td>
    `;
      employeeTableBody.appendChild(row);
    });

    currentPageSpan.textContent = currentPage;
  }

  // Функция для рендеринга пагинации
  function renderPagination() {
    const totalPages = Math.ceil(filteredContacts.length / itemsPerPage);
    totalPagesSpan.textContent = totalPages || 1;

    prevPageBtn.disabled = currentPage === 1;
    nextPageBtn.disabled = currentPage === totalPages || totalPages === 0;
  }

  // Обработчики пагинации
  prevPageBtn.addEventListener("click", () => {
    if (currentPage > 1) {
      currentPage--;
      renderTable();
      renderPagination();
      console.log(`Перейдено на страницу ${currentPage}`);
    }
  });

  nextPageBtn.addEventListener("click", () => {
    const totalPages = Math.ceil(filteredContacts.length / itemsPerPage);
    if (currentPage < totalPages) {
      currentPage++;
      renderTable();
      renderPagination();
      console.log(`Перейдено на страницу ${currentPage}`);
    }
  });

  // Обработчик фильтрации
  filterBtn.addEventListener("click", () => {
    const query = filterInput.value.toLowerCase().trim();
    if (query === "") {
      filteredContacts = contacts.slice();
    } else {
      filteredContacts = contacts.filter(
        (contact) =>
          contact.full_name.toLowerCase().includes(query) ||
          contact.job_description.toLowerCase().includes(query) ||
          contact.phone.toLowerCase().includes(query) ||
          contact.email.toLowerCase().includes(query),
      );
    }
    currentPage = 1;
    renderTable();
    renderPagination();
    console.log(`Фильтрация по запросу: "${query}"`);
  });

  // Обработчик сортировки
  document.querySelectorAll("#employee-table th[data-column]").forEach((header) => {
    header.addEventListener("click", () => {
      const column = header.dataset.column;
      if (currentSort.column === column) {
        currentSort.direction = currentSort.direction === "asc" ? "desc" : "asc";
      } else {
        currentSort.column = column;
        currentSort.direction = "asc";
      }
      sortContacts();
      renderTable();
      updateSortIndicators();
      console.log(`Сортировка по столбцу: "${column}", направление: "${currentSort.direction}"`);
    });
  });

  // Функция сортировки
  function sortContacts() {
    const { column, direction } = currentSort;
    if (!column) return;

    filteredContacts.sort((a, b) => {
      let aVal = a[column];
      let bVal = b[column];

      // Для строк
      if (typeof aVal === "string") {
        aVal = aVal.toLowerCase();
        bVal = bVal.toLowerCase();
      }

      if (aVal < bVal) return direction === "asc" ? -1 : 1;
      if (aVal > bVal) return direction === "asc" ? 1 : -1;
      return 0;
    });
  }

  // Функция обновления индикаторов сортировки
  function updateSortIndicators() {
    document.querySelectorAll("#employee-table th[data-column]").forEach((header) => {
      const indicator = header.querySelector(".sort-indicator");
      const column = header.dataset.column;
      if (column === currentSort.column) {
        indicator.textContent = currentSort.direction === "asc" ? " ▲" : " ▼";
      } else {
        indicator.textContent = "";
      }
    });
  }

  // Обработчик клика на строку таблицы для отображения деталей
  employeeTableBody.addEventListener("click", (event) => {
    const row = event.target.closest("tr");
    if (!row) return;

    const contactId = row.dataset.id;
    const contact = contacts.find((c) => c.id == contactId);
    if (contact) {
      employeeDetails.innerHTML = `
        <h3>Детали сотрудника</h3>
        <p><strong>ФИО:</strong> ${contact.full_name}</p>
        <p><strong>Описание работ:</strong> ${contact.job_description}</p>
        <p><strong>Телефон:</strong> ${contact.phone}</p>
        <p><strong>Почта:</strong> ${contact.email}</p>
        <img src="${contact.photo_url}" alt="Фото" width="100">
      `;
      employeeDetails.classList.add("active");
      console.log(`Отображение деталей для сотрудника: ${contact.full_name}`);
    }
  });

  // Обработчики модального окна
  addEmployeeBtn.addEventListener("click", () => {
    console.log("Add Employee button clicked");
    addEmployeeModal.classList.add("active");
  });

  modalClose.addEventListener("click", () => {
    console.log("Modal close button clicked");
    addEmployeeModal.classList.remove("active");
    resetForm();
  });

  window.addEventListener("click", (event) => {
    if (event.target === addEmployeeModal) {
      console.log("Clicked outside modal");
      addEmployeeModal.classList.remove("active");
      resetForm();
    }
  });

  // Валидация URL
  photoUrlInput.addEventListener("input", () => {
    const url = photoUrlInput.value;
    const pattern = /^(http:\/\/|https:\/\/).+\.(php|html)$/i;
    if (pattern.test(url)) {
      photoUrlError.classList.remove("active");
      photoUrlInput.style.borderColor = "";
      photoUrlInput.style.backgroundColor = "";
      console.log("Photo URL valid");
    } else {
      photoUrlError.textContent = "Некорректный URL. Пример: http://site.ru/index.php";
      photoUrlError.classList.add("active");
      photoUrlInput.style.borderColor = "#c40000";
      photoUrlInput.style.backgroundColor = "#ff4fce";
      console.log("Photo URL invalid");
    }
    validateForm();
  });

  // Валидация телефона
  phoneInput.addEventListener("input", () => {
    const phone = phoneInput.value;
    const pattern =
      /^(80|\+375)\s?\(?\d{2,3}\)?\s?\d{3}[-\s]?\d{2}[-\s]?\d{2}$|^(8)\s?\(?\d{3}\)?\s?\d{3}[-\s]?\d{2}[-\s]?\d{2}$|^(80|\+375)\s?\(?\d{2,3}\)?\s?\d{7}$/;

    if (pattern.test(phone)) {
      phoneError.classList.remove("active");
      phoneInput.style.borderColor = "";
      phoneInput.style.backgroundColor = "";
      console.log("Phone number valid");
    } else {
      phoneError.textContent = "Некорректный номер телефона.";
      phoneError.classList.add("active");
      phoneInput.style.borderColor = "#c40000"; // Темно-красный цвет обводки
      phoneInput.style.backgroundColor = "#ff4fce"; // Светло-розовый фон
      console.log("Phone number invalid");
    }
    validateForm();
  });

  // Устанавливаем начальное состояние кнопки (неактивная)
  submitEmployeeBtn.disabled = true;
  submitEmployeeBtn.classList.add("inactive-btn");

  // Функция проверки формы
  function validateForm() {
    const isPhotoUrlValid =
      !photoUrlError.classList.contains("active") && photoUrlInput.value.trim() !== "";
    const isPhoneValid = !phoneError.classList.contains("active") && phoneInput.value.trim() !== "";
    const isFullNameValid = fullNameInput.value.trim() !== "";
    const isJobDescValid = jobDescriptionInput.value.trim() !== "";
    const isEmailValid = emailInput.value.trim() !== "";

    // Активируем кнопку, если все поля валидны, иначе — оставляем неактивной
    if (isPhotoUrlValid && isPhoneValid && isFullNameValid && isJobDescValid && isEmailValid) {
      submitEmployeeBtn.disabled = false;
      submitEmployeeBtn.classList.remove("inactive-btn");
    } else {
      submitEmployeeBtn.disabled = true;
      submitEmployeeBtn.classList.add("inactive-btn");
    }

    console.log(
      `Form validation: photoUrlValid=${isPhotoUrlValid}, phoneValid=${isPhoneValid}, fullNameValid=${isFullNameValid}, jobDescValid=${isJobDescValid}, emailValid=${isEmailValid}`,
    );
  }

  photoUrlInput.addEventListener("input", validateForm);
  phoneInput.addEventListener("input", validateForm);
  fullNameInput.addEventListener("input", validateForm);
  jobDescriptionInput.addEventListener("input", validateForm);
  emailInput.addEventListener("input", validateForm);

  // Обработчик отправки формы
  addEmployeeForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    console.log("Form submitted");

    const formData = {
      full_name: fullNameInput.value.trim(),
      photo_url: photoUrlInput.value.trim(),
      job_description: jobDescriptionInput.value.trim(),
      phone: phoneInput.value.trim(),
      email: emailInput.value.trim(),
    };

    console.log("Form Data:", formData);

    try {
      const response = await fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCSRFToken(),
        },
        body: JSON.stringify(formData),
      });

      console.log("Response Status:", response.status);

      if (response.ok) {
        const newContact = await response.json();
        contacts.push(newContact);
        filteredContacts = contacts.slice();
        renderTable();
        renderPagination();
        formResult.textContent = "Сотрудник успешно добавлен!";
        formResult.style.color = "#2ecc71";
        resetForm();
        console.log(`Новый сотрудник добавлен: ${newContact.full_name}`);
        setTimeout(() => {
          formResult.textContent = "";
        }, 3000);
      } else {
        const errorData = await response.json();
        formResult.textContent = "Ошибка при добавлении сотрудника.";
        formResult.style.color = "#e74c3c";
        console.log("Error Data:", errorData);
      }
    } catch (error) {
      console.error("Ошибка при отправке формы:", error);
      formResult.textContent = "Ошибка при добавлении сотрудника.";
      formResult.style.color = "#e74c3c";
    }
  });

  // Функция сброса формы
  function resetForm() {
    addEmployeeForm.reset();
    photoUrlError.classList.remove("active");
    phoneError.classList.remove("active");
    submitEmployeeBtn.disabled = true;
    formResult.textContent = "";
    photoUrlInput.style.borderColor = "";
    photoUrlInput.style.backgroundColor = "";
    phoneInput.style.borderColor = "";
    phoneInput.style.backgroundColor = "";
    console.log("Form reset");
  }

  // Функция получения CSRF токена
  function getCSRFToken() {
    const cookieValue = document.cookie.match("(^|;)\\s*csrftoken\\s*=\\s*([^;]+)");
    return cookieValue ? cookieValue.pop() : "";
  }

  // Обработчик для чекбоксов
  employeeTableBody.addEventListener("change", (event) => {
    const checkbox = event.target;
    if (checkbox.classList.contains("select-checkbox")) {
      const employeeId = parseInt(checkbox.value);
      if (checkbox.checked) {
        if (!selectedEmployees.includes(employeeId)) {
          selectedEmployees.push(employeeId);
        }
      } else {
        selectedEmployees = selectedEmployees.filter((id) => id !== employeeId);
      }
      console.log("Selected employees:", selectedEmployees);
    }
  });

  // Обработчик премирования
  awardBtn.addEventListener("click", () => {
    if (selectedEmployees.length === 0) {
      awardText.textContent = "Нет выбранных сотрудников для премирования.";
      awardText.classList.add("active");
      console.log("No employees selected for awarding");
      return;
    }

    const selectedNames = contacts
      .filter((contact) => selectedEmployees.includes(contact.id))
      .map((contact) => contact.full_name);

    const namesString = selectedNames.join(", ");
    awardText.textContent = `Поздравляем сотрудников: ${namesString} с заслуженной премией!`;
    awardText.classList.add("active");
    console.log(`Awarded employees: ${namesString}`);

    // Скрыть сообщение через 5 секунд
    setTimeout(() => {
      awardText.classList.remove("active");
      console.log("Award message hidden");
    }, 5000);
  });

  // Инициализация загрузки данных
  loadContacts();
});
