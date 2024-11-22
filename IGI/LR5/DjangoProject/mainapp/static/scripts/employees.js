document.addEventListener("DOMContentLoaded", function() {
    const rowsPerPage = 3; 
    let rows = Array.from(document.querySelectorAll('.employee-row'));
    let currentPage = 1;  

    function showPage(page) {
        const filteredRows = rows.filter(row => row.getAttribute('data-included') === 'on'); 

        rows.forEach(row => row.style.display = 'none');
        
        filteredRows.forEach((row, index) => {
            const start = (page - 1) * rowsPerPage;
            const end = page * rowsPerPage;
            row.style.display = (index >= start && index < end) ? '' : 'none';
        });
    }

    function updatePagination() {
        const paginationElement = document.getElementById('pagination');
        paginationElement.innerHTML = '';

        const filteredRows = rows.filter(row => row.getAttribute('data-included') === 'on');
        const totalPages = Math.ceil(filteredRows.length / rowsPerPage);  

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

    function filterRows(searchText) {
        rows.forEach(row => {
            let isMatch = false;
            row.querySelectorAll('td').forEach(cell => {
                if (cell.innerText.toLowerCase().includes(searchText.toLowerCase())) {
                    isMatch = true;
                }
            });

            row.setAttribute('data-included', isMatch ? 'on' : 'off');
        });

        currentPage = 1;
        showPage(currentPage);
        updatePagination();
    }

    const searchButton = document.getElementById('search-button');
    const searchInput = document.getElementById('search-input');
    searchButton.addEventListener('click', function() {
        const searchText = searchInput.value;
        filterRows(searchText);  
    });

    showPage(currentPage);
    updatePagination();


    const addEmployeeBtn = document.getElementById("add-employee-btn");
    const addEmployeeForm = document.getElementById("add-employee-form");
    const employeeForm = document.getElementById("employee-form");
    const validationMessage = document.getElementById("validation-message");

  addEmployeeBtn.addEventListener("click", function () {
    addEmployeeForm.style.display = addEmployeeForm.style.display === "none" ? "block" : "none";
  });

  function validateURL(url) {
    const regex = /^(http:\/\/|https:\/\/).*\.(php|html)$/;
    return regex.test(url);
  }

  function validatePhone(phone) {
    const regex = /^(\+375|8)\s*\(?\d{2}\)?\s*\d{3}[- ]?\d{2}[- ]?\d{2}$/;
    return regex.test(phone);
  }

  employeeForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const fullName = document.getElementById("full-name").value;
    const jobDesc = document.getElementById("job-desc").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
    const url = document.getElementById("url").value;
    const photo = document.getElementById("photo").files[0];

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

    validationMessage.textContent = "";
    document.getElementById("url").style.border = "";
    document.getElementById("url").style.backgroundColor = "";
    document.getElementById("phone").style.border = "";
    document.getElementById("phone").style.backgroundColor = "";

    const newRow = document.createElement("tr");
    newRow.classList.add("employee-row");
    newRow.setAttribute("data-included", "on");

    newRow.innerHTML = `
      <td><img src="${URL.createObjectURL(photo)}" alt="Photo" class="employee-img" style="width: 50px; height: 50px;"/></td>
      <td>${fullName}</td>
      <td>${jobDesc}</td>
      <td>${email}</td>
      <td>${phone}</td>
      <td>${url}</td>
      <td><input type="checkbox" name="employee_select"></td>
    `;

    document.querySelector(".employee-table tbody").appendChild(newRow);

    employeeForm.reset();
    addEmployeeForm.style.display = "none";

    rows = Array.from(document.querySelectorAll(".employee-row")); 
    currentPage = 1;
    showPage(currentPage);
    updatePagination();
  });

  document.getElementById('premium-button').addEventListener('click', function() {
    console.log('ступапупа')
    const loader = document.querySelector('.loader');
    const premiumBody = document.getElementById('premium-body');
    loader.style.display = 'block';
    premiumBody.innerHTML = '';

    const selectedEmployees = document.querySelectorAll('.employee-row input[type="checkbox"]:checked');
    const employeeNames = Array.from(selectedEmployees).map(checkbox => {
      const row = checkbox.closest('.employee-row');
      const fullName = row.children[1].textContent;
      return fullName;
    });

    
    setTimeout(() => {
      loader.style.display = 'none'; 
      if (employeeNames.length > 0) {
        
        const text = `Сотрудники ${employeeNames.join(', ')} были премированы за выдающиеся успехи и вклад в компанию.`;
        premiumBody.innerHTML = `<p class="premium-text">${text}</p>`;
      } else {
        
        premiumBody.innerHTML = '<p class="premium-text">Не выбраны сотрудники для премирования.</p>';
      }
    }, 3000);
  });
});



function sortTable(columnIndex) {
    const table = document.querySelector('.employee-table');
    const rows = Array.from(table.querySelectorAll('tbody tr'));
  
    const isAscending = table.querySelectorAll('th')[columnIndex].classList.contains('ascending');
  
    table.querySelectorAll('th').forEach(th => th.classList.remove('ascending', 'descending'));
  
    if (isAscending) {
      table.querySelectorAll('th')[columnIndex].classList.add('descending');
    } else {
      table.querySelectorAll('th')[columnIndex].classList.add('ascending');
    }
  
    rows.sort((rowA, rowB) => {
      const cellA = rowA.cells[columnIndex].innerText.trim();
      const cellB = rowB.cells[columnIndex].innerText.trim();
  
      if (isAscending) {
        return cellA > cellB ? -1 : 1; 
      } else {
        return cellA < cellB ? -1 : 1; 
      }
    });
  
    rows.forEach(row => table.querySelector('tbody').appendChild(row));
  }
  
  function toggleDetails(row) {
    var detailsDiv = document.getElementById('employee-details');
    
    if (detailsDiv.style.display === 'block') {
        detailsDiv.style.display = 'none';
    } else {
        var cells = row.getElementsByTagName('td');
        
        var photo = cells[0].querySelector('img').src; 
        var name = cells[1].innerText; 
        var jobDescription = cells[2].innerText; 
        var email = cells[3].innerText;  
        var phoneNumber = cells[4].innerText; 
        var profileUrl = cells[5].innerText;  

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

