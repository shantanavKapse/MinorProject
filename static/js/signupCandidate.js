function showpasswd() {
  let x = document.getElementById("passwd");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function chngPage1() {
  document.querySelector(".page1").style.display = "none";
  document.querySelector(".page2").style.display = "block";
}

function backPage2() {
  document.querySelector(".page1").style.display = "block";
  document.querySelector(".page2").style.display = "none";
}

function chngPage2() {
  document.querySelector(".page2").style.display = "none";
  document.querySelector(".page3").style.display = "block";
}

function backPage3() {
  document.querySelector(".page3").style.display = "none";
  document.querySelector(".page2").style.display = "block";
}

function showProfileImage(){
  const profileImage = document.querySelector('#pro-photo');
  document.querySelector('#profile-label').textContent = profileImage.files[0].name;
}

function showFileName(){
  const resume = document.querySelector('#resume');
  document.querySelector('#resume-label').textContent = resume.files[0].name;
}

const myInput = document.getElementById("passwd");
const infoIcon = document.querySelector(".info-icon");
const msgReq = document.querySelector(".msg-req");
const letter = document.getElementById("letter");
const capital = document.getElementById("capital");
const number = document.getElementById("number");
const length = document.getElementById("length");
const special = document.getElementById("specialChar");

const reg = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,15})/;
myInput.onkeyup = function () {
  if (myInput.value.match(reg)) {
    msgReq.style.display = "none";
    infoIcon.style.display = "none";
  } else {
    msgReq.style.display = "block";
    infoIcon.style.display = "block";
  }

  const lowerCaseLetters = /[a-z]/g;
  if (myInput.value.match(lowerCaseLetters)) {
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
  }

  const upperCaseLetters = /[A-Z]/g;
  if (myInput.value.match(upperCaseLetters)) {
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  const specialCharacter = /[!@#\$%\^&\*]/g;
  if (myInput.value.match(specialCharacter)) {
    special.classList.remove("invalid");
    special.classList.add("valid");
  } else {
    special.classList.remove("valid");
    special.classList.add("invalid");
  }

  const numbers = /[0-9]/g;
  if (myInput.value.match(numbers)) {
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }

  if (myInput.value.length >= 8 && myInput.value.length <=15) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
};
