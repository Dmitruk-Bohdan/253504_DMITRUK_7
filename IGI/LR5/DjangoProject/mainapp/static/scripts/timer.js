document.addEventListener("DOMContentLoaded", () => {
  console.log('Таймер загружен');

  const hoursElement = document.getElementById("hours");
  const minutesElement = document.getElementById("minutes");
  const secondsElement = document.getElementById("seconds");

  let remainingTime = localStorage.getItem("remainingTime");

  if (!remainingTime) {
    remainingTime = 60 * 60 * 1000;
  } else {
    remainingTime = parseInt(remainingTime);
  }

  function runTimer() {
    function refreshDisplayTime() {
      if (remainingTime <= 0) {
        hoursElement.textContent = "00";
        minutesElement.textContent = "00";
        secondsElement.textContent = "00";
        clearInterval(timerInterval);
        return;
      }

      const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

      hoursElement.textContent = hours.toString().padStart(2, "0");
      minutesElement.textContent = minutes.toString().padStart(2, "0");
      secondsElement.textContent = seconds.toString().padStart(2, "0");
      remainingTime -= 1000;
    }

    refreshDisplayTime();
    const timerInterval = setInterval(refreshDisplayTime, 1000);
  }

  window.addEventListener("beforeunload", () => {
    localStorage.setItem("remainingTime", remainingTime);
  });

  runTimer();
});
