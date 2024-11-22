document.addEventListener('DOMContentLoaded', () => {
    function solveCos(x, eps) {
        let C = 1; // Начальное значение для суммы ряда
        let i = 1; // Порядковый номер слагаемого
        let q = 1; // Начальное значение слагаемого
        let iterations = 0;
    
        // Пока очередное слагаемое больше погрешности
        while (Math.abs(q) > eps && iterations <= 500) {
            q = q * (-1) * (x * x) / ((2 * i - 1) * (2 * i)); // Следующее слагаемое
            C += q;
            i += 1;
            iterations += 1;
        }
    
        return C;
    }

    // Функция для генерации данных для косинуса
    function generateCosData(eps) {
        const labels = [];
        const dataCos = [];
      
        let q = 0.05;
        for (let x = -Math.PI; x <= Math.PI; x += q) { // Генерация для значений от -π до π
            labels.push(x.toFixed(2)); // Значения для оси X
            dataCos.push(solveCos(x, eps)); // Результаты вычисления косинуса
        }
    
        return { labels, dataCos };
    }

    // Функция для обновления графика при изменении значений из формы
    function updateChart() {
        const eps = parseFloat(document.getElementById('epsilon').value); // Получаем погрешность из формы
        if (isNaN(eps) || eps <= 0) {
            alert('Введите корректное значение для погрешности (ε).');
            return;
        }
        
        const { labels, dataCos } = generateCosData(eps);

        // default Math.cos
        const dataMathCos = labels.map(label => Math.cos(parseFloat(label)));

        // Построение графика
        let delayed;
        const plot = document.getElementById("myChart").getContext("2d");
        const myChart = new Chart(plot, {
            type: "line",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: "cos(x) с ряд Тейлора",
                        data: dataCos,
                        borderColor: "rgba(0, 0, 255, 0.5)",
                        backgroundColor: "rgba(0, 0, 255, 0.2)",
                        fill: false,
                        tension: 0.1,
                    },
                    {
                        label: "cos(x) Math.cos",
                        data: dataMathCos,
                        borderColor: "rgba(255, 0, 0, 0.5)",
                        backgroundColor: "rgba(255, 0, 0, 0.2)",
                        fill: false,
                        tension: 0.1,
                    },
                ],
            },
            options: {
                responsive: true, // График будет адаптироваться под размер контейнера
                animation: {
                    onComplete: () => {
                        delayed = true; // Блокируем повторное срабатывание анимации для точек
                    },
                    delay: (context) => {
                        let delay = 0;
                        if (context.type === 'data' && context.mode === 'default' && !delayed) {
                            // Изменение задержки для анимации справа налево
                            delay = (labels.length - context.dataIndex) * 80 + context.datasetIndex * 100;
                        }
                        return delay;
                    },
                },
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: "x (radians)",
                        },
                        ticks: {
                            stepSize: Math.PI / 2, // Шаг на оси X (π/2)
                        },
                    },
                    y: {
                        title: {
                            display: true,
                            text: "y",
                        },
                    },
                },
            },
        });
    }

    // Инициализация графика при загрузке страницы
    updateChart();

    // Обработчик события для формы
    document.getElementById("inputForm").addEventListener("submit", (event) => {
        event.preventDefault(); // Отменяем стандартное поведение формы
        updateChart(); // Обновляем график при изменении погрешности
    });

    // Сохранение графика в изображение
    document.getElementById('saveLink').addEventListener('click', function() {
        const link = document.getElementById("saveLink");
        link.href = document.getElementById("myChart").toDataURL('image/png');
    });
});
