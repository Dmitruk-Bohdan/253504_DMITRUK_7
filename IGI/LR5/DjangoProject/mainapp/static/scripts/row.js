document.addEventListener('DOMContentLoaded', () => {
    function solveCos(x, eps) {
        let C = 1;
        let i = 1;
        let q = 1;
        let prevC = 0;
        let iterations = 0;

        while (Math.abs(C - prevC) > eps && iterations <= 500) {
            prevC = C;
            q = q * (-1) * (x * x) / ((2 * i - 1) * (2 * i)); 
            C += q;
            i += 1;
            iterations += 1;
        }

        return C;
    }

    function generateCosData(eps) {
        const labels = [];
        const dataCos = [];
      
        let q = 0.05;
        for (let x = -2 * Math.PI; x <= 2 * Math.PI; x += q) {
            labels.push(x.toFixed(2)); 
            dataCos.push(solveCos(x, eps));
        }
    
        return { labels, dataCos };
    }

    function updateChart() {
        const eps = parseFloat(document.getElementById('epsilon').value); 
        if (isNaN(eps) || eps <= 0) {
            alert('Введите корректное значение для погрешности (ε).');
            return;
        }
        
        const { labels, dataCos } = generateCosData(eps);

        const dataMathCos = labels.map(label => Math.cos(parseFloat(label)));

        const plot = document.getElementById("myChart").getContext("2d");

        if (window.myChart instanceof Chart) {
            window.myChart.destroy();
        }

        window.myChart = new Chart(plot, {
            type: "line",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: "Разложение cos(x) в ряд",
                        data: dataCos,
                        borderColor: "rgba(255, 165, 0, 0.5)", 
                        backgroundColor: "rgba(255, 165, 0, 0.2)",
                        fill: false,
                        tension: 0.1,
                        pointRadius: 0,
                    },
                    {
                        label: "Math.cos",
                        data: dataMathCos,
                        borderColor: "rgba(0, 128, 0, 0.5)", 
                        backgroundColor: "rgba(0, 128, 0, 0.2)",
                        fill: false,
                        tension: 0.1,
                        pointRadius: 0,
                    },
                ],
            },
            options: {
                responsive: true, 
                animation: {
                    delay: (context) => {
                        delay = context.dataIndex * 80 + context.datasetIndex * 100;
                        return delay;
                    },
                },
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: "x в радианах",
                        },
                        ticks: {
                            stepSize: Math.PI / 2, 
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

    updateChart();

    document.getElementById("inputForm").addEventListener("submit", (event) => {
        event.preventDefault();
        updateChart(); 
    });

});
