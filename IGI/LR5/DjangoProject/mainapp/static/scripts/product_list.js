document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll('.product-card-wrapper');

    cards.forEach(cardWrapper => {
    const card = cardWrapper.querySelector('.product-card');

    cardWrapper.addEventListener('mousemove', (event) => {
        const rect = cardWrapper.getBoundingClientRect();
        const [width, height] = [rect.width, rect.height];
        const middleX = width / 2;
        const middleY = height / 2;

        const offsetX = ((event.offsetX - middleX) / middleX) * 20;  
        const offsetY = ((event.offsetY - middleY) / middleY) * 20;

        const posX = 50 + ((event.offsetX - middleX) / middleX) * 15;
        const posY = 50 - ((event.offsetY - middleY) / middleY) * 15;

        card.style.transform = `rotateY(${offsetX}deg) rotateX(${offsetY}deg)`;
        card.style.backgroundPosition = `${posX}% ${posY}%`;
    });

    cardWrapper.addEventListener('mouseleave', () => {
        card.style.transform = 'rotateY(0deg) rotateX(0deg)';
        card.style.backgroundPosition = '50% 50%';
    });
    });


    const itemsPerPage = 3; 
    const products = document.querySelectorAll(".product-card-wrapper");
    const paginationContainer = document.querySelector(".pagination-container");
    let currentPage = 1;
    const totalPages = Math.ceil(products.length / itemsPerPage);

    function displayItems(page) {
        products.forEach((product, index) => {
            product.style.display = "none";
            const start = (page - 1) * itemsPerPage;
            const end = start + itemsPerPage;
            if (index >= start && index < end) {
                product.style.display = "block";
            }
        });
    }

    function setupPagination() {
        paginationContainer.innerHTML = "";
        for (let i = 1; i <= totalPages; i++) {
            const button = document.createElement("button");
            button.textContent = i;
            button.classList.add("pagination-button");
            if (i === currentPage) button.classList.add("active");
            button.addEventListener("click", () => {
                currentPage = i;
                displayItems(currentPage);
                document.querySelector(".pagination-button.active").classList.remove("active");
                button.classList.add("active");
            });
            paginationContainer.appendChild(button);
        }
    }

    displayItems(currentPage);
    setupPagination();
});
