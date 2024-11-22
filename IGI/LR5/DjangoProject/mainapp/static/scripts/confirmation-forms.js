document.addEventListener("DOMContentLoaded", function() {
    window.checkAge = function() {
        const dobInput = document.getElementById('dob').value;
        const resultDiv = document.getElementById('confirmation-result');

        if (!dobInput) {
            resultDiv.innerHTML = "<div class='alert'>Пожалуйста, введите дату рождения.</div>";
            return;
        }

        const dob = new Date(dobInput);
        const today = new Date();
        let age = today.getFullYear() - dob.getFullYear();
        const m = today.getMonth() - dob.getMonth();
        if (m < 0 || (m === 0 && today.getDate() < dob.getDate())) {
            age--;
        }

        const daysOfWeek = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'];
        const dayOfWeek = daysOfWeek[dob.getDay()];

        const ageMessage = age >= 18 
            ? `<div class='success'>Вам ${age} лет. День вашего рождения — ${dayOfWeek}.</div>`
            : `<div class='alert'>Вам ${age} лет. Вы несовершеннолетний. Для использования сайта вам необходимо разрешение родителей.</div>`;

        resultDiv.innerHTML = ageMessage;
    }
});