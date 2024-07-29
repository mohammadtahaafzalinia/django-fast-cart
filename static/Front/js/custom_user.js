let secondsRemaining = 115;

function updateCountdown() {
  document.getElementById('countdown_otp').innerHTML = secondsRemaining + ' ثانیه';
  secondsRemaining--;

  if (secondsRemaining < 0) {
    clearInterval(intervalId);
    document.getElementById('countdown_otp').innerHTML = 'تمام شد';
  }
}

updateCountdown(); // نمایش اولیه
const intervalId = setInterval(updateCountdown, 1000);