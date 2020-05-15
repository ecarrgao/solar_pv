var index = 0;

function slideShow() {
  var i;
  var x = document.getElementsByClassName("event");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  index++;
  if (index > x.length) {
    index = 1;
  }
  x[index-1].style.display = "block";
  setTimeout(slideShow, 5000);
}

function validatePassword() {
  var password = document.getElementById('password');
  var regex = /^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])/;
  if (regex.test(password.value)) {
    return true;
  }
  else {
    alert("Password must be at most 8 characters long comprising at least a digit, a lowercase letter, and an uppercase letter.");
  }
}
