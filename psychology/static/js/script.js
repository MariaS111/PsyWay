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

document.addEventListener("DOMContentLoaded", function() {
    var saveButton = document.getElementById("save_button");
    var isConfirmedCheckbox = document.getElementById("is_confirmed_checkbox");
    console.log('work')
    saveButton.addEventListener("click", function() {
        var isConfirmed = isConfirmedCheckbox.checked;

        var data = {
            'is_confirmed': isConfirmed ? '1' : '0'
        };

        var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

        var xhr = new XMLHttpRequest();
        xhr.open("POST", "", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.setRequestHeader("X-CSRFToken", csrfToken);
        console.log('good work')
        xhr.onload = function() {
    console.log("onload event occurred");
    console.log("Status: " + xhr.status);
    if (xhr.status === 200) {
        console.log("Изменения сохранены успешно");
    } else {
        console.log("Произошла ошибка при сохранении изменений");
    }
};
        xhr.send(JSON.stringify(data));
    });
});

//
//
// var openButton1 = document.getElementById("open_requests");
//
// var closeButton1 = document.getElementsByClassName("close1")[0];
// // Найти контейнер окна
// var modal1 = document.getElementById("my_requests");
//
// openButton1.onclick = function() {
//   modal1.style.display = "block";
//   console.log('success')
// }
//
// // Закрыть окно при нажатии на элемент закрытия
// closeButton1.onclick = function() {
//   modal1.style.display = "none";
// }
//
// // Закрыть окно, если пользователь кликнул за его пределами
// window.onclick = function(event) {
//   if (event.target == modal1) {
//     modal1.style.display = "none";
//   }
// }


