// Найти кнопку открытия окна
var openButton = document.getElementById("open_sessions");

// Найти контейнер окна
var modal = document.getElementById("my_sessions");

// Найти элемент закрытия окна
var closeButton = document.getElementsByClassName("close")[0];

// Открыть окно при нажатии на кнопку
openButton.onclick = function() {
  modal.style.display = "block";
}

// Закрыть окно при нажатии на элемент закрытия
closeButton.onclick = function() {
  modal.style.display = "none";
}

// Закрыть окно, если пользователь кликнул за его пределами
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
