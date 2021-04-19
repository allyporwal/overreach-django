let timer = 0;

$("#rest-timer").click(function () {
  $("#rest-timer-overlay").fadeToggle(250);
});

$("#close-timer").click(function () {
  $("#rest-timer-overlay").fadeToggle(250);
});

$(".btn-timer").click(function () {
  let seconds = $(this).text().slice(0, -1);
  countdownTimer.countdown(seconds);
  displayCountdown();
});

let countdownTimer = {
  countdown: function (seconds) {
    this.counter = seconds;
    clearInterval(this.timerInterval);
    this.timerInterval = setInterval(() => {
      this.counter--;
      if (this.counter == 0) {
        clearInterval(this.timerInterval);  
      }
    }, 1000);
  },
};

function displayCountdown() {
  setInterval(function () {
    $("#timer-display").text(`${countdownTimer.counter}`);
  }, 1000);
}
