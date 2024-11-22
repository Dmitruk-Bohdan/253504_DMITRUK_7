class WorkClass {
    constructor(name, author, year, style) {
        this._name = name;
        this._author = author;
        this._year = year;
        this._style = style;
    }

    get name() {
        return this._name;
    }

    set name(value) {
        this._name = value;
    }

    get author() {
        return this._author;
    }

    set author(value) {
        this._author = value;
    }

    get year() {
        return this._year;
    }

    set year(value) {
        this._year = value;
    }

    get style() {
        return this._style;
    }

    set style(value) {
        this._style = value;
    }
}

class BookClass extends WorkClass {
    constructor(name, author, year, style, pages, publisher, language) {
        super(name, author, year, style);
        this._pages = pages;
        this._publisher = publisher;
        this._language = language;
    }

    get pages() {
        return this._pages;
    }

    set pages(value) {
        this._pages = value;
    }

    get publisher() {
        return this._publisher;
    }

    set publisher(value) {
        this._publisher = value;
    }

    get language() {
        return this._language;
    }

    set language(value) {
        this._language = value;
    }

    static createBook(name, author, year, style, pages, publisher, language) {
        return new BookClass(name, author, year, style, pages, publisher, language);
    }
}

let booksClass = [];
let authorsClass = [];

function addBookFromFormClass() {
  const name = document.getElementById('name-class').value;
  const author = document.getElementById('author-class').value;
  const year = document.getElementById('year-class').value;
  const style = document.getElementById('style-class').value;
  const pages = document.getElementById('pages-class').value;
  const publisher = document.getElementById('publisher-class').value;
  const language = document.getElementById('language-class').value;

  const newBook = BookClass.createBook(name, author, year, style, pages, publisher, language);
  booksClass.push(newBook);

  if (!authorsClass.includes(author)) {
    authorsClass.push(author);
    updateAuthorSelectClass();
  }

  displayBooksClass();
  filterBooksByAuthorClass();
}

function updateAuthorSelectClass() {
  const authorSelect = document.getElementById('author-select-class');
  authorSelect.innerHTML = '';

  const allOption = document.createElement('option');
  allOption.value = '';
  allOption.textContent = 'Все авторы';
  authorSelect.appendChild(allOption);

  authorsClass.forEach(author => {
    const option = document.createElement('option');
    option.value = author;
    option.textContent = author;
    authorSelect.appendChild(option);
  });
}

function displayBooksClass() {
  const outputDiv = document.getElementById('books-output-class');
  outputDiv.innerHTML = '';

  booksClass.forEach(book => {
    outputDiv.innerHTML += `
      <p>Название: ${book.name} - Автор: ${book.author} - Год: ${book.year} - Стиль: ${book.style} - Страницы: ${book.pages} - Издательство: ${book.publisher} - Язык: ${book.language}</p>
    `;
  });
}

function filterBooksByAuthorClass() {
    debugger;
    const selectedAuthor = document.getElementById('author-select-class').value;
    
    const filteredBooks = booksClass.filter(book => {
      const isAuthorMatch = selectedAuthor ? book.author === selectedAuthor : true;
      const isYearValid = book.year >= 1980;
      return isAuthorMatch && isYearValid;
    });
  
    const outputDiv = document.getElementById('filter-output-class');
    outputDiv.innerHTML = '';
    filteredBooks.forEach(book => {
      outputDiv.innerHTML += `
        <p>Автор: ${book.author}, Год: ${book.year}, Стиль: ${book.style}</p>
      `;
    });
  }
