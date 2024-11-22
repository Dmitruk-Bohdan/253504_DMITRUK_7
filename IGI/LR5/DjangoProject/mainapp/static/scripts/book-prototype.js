function WorkPrototype(name, author, year, style) {
    this.name = name;
    this.author = author;
    this.year = year;
    this.style = style;
}

WorkPrototype.prototype.getName = function() {
    return this.name;
};
WorkPrototype.prototype.setName = function(name) {
    this.author = name;
};

WorkPrototype.prototype.getAuthor = function() {
    return this.author;
};
WorkPrototype.prototype.setAuthor = function(author) {
    this.author = author;
};

WorkPrototype.prototype.getYear = function() {
    return this.year;
};
WorkPrototype.prototype.setYear = function(year) {
    this.year = year;
};

WorkPrototype.prototype.getStyle = function() {
    return this.style;
};
WorkPrototype.prototype.setStyle = function(style) {
    this.style = style;
};

function BookPrototype(author, year, style, pages, publisher, language) {
    WorkPrototype.call(this, author, year, style);
    this.pages = pages;
    this.publisher = publisher;
    this.language = language;
}

BookPrototype.prototype = Object.create(WorkPrototype.prototype);
BookPrototype.prototype.constructor = BookPrototype;

BookPrototype.prototype.getPages = function() {
    return this.pages;
};
BookPrototype.prototype.setPages = function(pages) {
    this.pages = pages;
};

BookPrototype.prototype.getPublisher = function() {
    return this.publisher;
};
BookPrototype.prototype.setPublisher = function(publisher) {
    this.publisher = publisher;
};

BookPrototype.prototype.getLanguage = function() {
    return this.language;
};
BookPrototype.prototype.setLanguage = function(language) {
    this.language = language;
};

let books = [];

let authors = [];

function addBookFromForm() {
  const name = document.getElementById('name').value;
  const author = document.getElementById('author').value;
  const year = document.getElementById('year').value;
  const style = document.getElementById('style').value;
  const pages = document.getElementById('pages').value;
  const publisher = document.getElementById('publisher').value;
  const language = document.getElementById('language').value;

  const newBook = new BookPrototype(name, author, year, style, pages, publisher, language);
  books.push(newBook);

  if (!authors.includes(author)) {
    authors.push(author);
    updateAuthorSelect();
  }

  displayBooks();
  filterBooksByAuthor();
}

function updateAuthorSelect() {
  const authorSelect = document.getElementById('author-select');
  authorSelect.innerHTML = '';

  const allOption = document.createElement('option');
  allOption.value = '';
  allOption.textContent = 'Все авторы';
  authorSelect.appendChild(allOption);

  authors.forEach(author => {
    const option = document.createElement('option');
    option.value = author;
    option.textContent = author;
    authorSelect.appendChild(option);
  });
}

function filterBooksByAuthor() {
    const selectedAuthor = document.getElementById('author-select').value;
  
    const filteredBooks = books.filter(book => {
      const isAuthorMatch = selectedAuthor ? book.getAuthor() === selectedAuthor : true;
      const isYearValid = book.getYear() >= 1980;
      return isAuthorMatch && isYearValid;
    });
  
    const outputDiv = document.getElementById('filter-output');
    outputDiv.innerHTML = '';
    filteredBooks.forEach(book => {
      outputDiv.innerHTML += `
        <p>${book.getName()} - ${book.getAuthor()} - ${book.getYear()}</p>
      `;
    });
  }
  

function displayBooks() {
  const outputDiv = document.getElementById('books-output');
  outputDiv.innerHTML = '';
  books.forEach(book => {
    outputDiv.innerHTML += `
      <p>Название: ${book.getName()} - Автор: ${book.getAuthor()} - Год: ${book.getYear()} - Стиль: ${book.getStyle()} - Страницы: ${book.getPages()} pages - Издательство: ${book.getPublisher()} - Язык: ${book.getLanguage()}</p>
    `;
  });
}
