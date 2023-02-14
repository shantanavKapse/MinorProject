function showpasswd() {
    let x = document.getElementById("passwd");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
    }

function chngPage1(){
    document.querySelector('.page1').style.display = "none";
    document.querySelector('.page2').style.display = "block";
}

function backPage2(){
    document.querySelector('.page1').style.display = "block";
    document.querySelector('.page2').style.display = "none";
}

function chngPage2(){
    document.querySelector('.page2').style.display = "none";
    document.querySelector('.page3').style.display = "block";
}

function backPage3(){
    document.querySelector('.page3').style.display = "none";
    document.querySelector('.page2').style.display = "block";
}

const myInput = document.getElementById("passwd");
const reqButton = document.getElementById("pass-req-button");
const msgBox = document.getElementById("message");
const letter = document.getElementById("letter");
const capital = document.getElementById("capital");
const number = document.getElementById("number");
const length = document.getElementById("length");

myInput.onfocus = function() {
    if(length.classList.contains("valid") && letter.classList.contains("valid") && capital.classList.contains("valid") && number.classList.contains("valid")){
        reqButton.style.display = "none";
    }
    else{
        reqButton.style.display = "block";
        reqButton.style.borderColor = "red"
    }
}

reqButton.onclick = function(){
    if(msgBox.style.display == "none"){
        msgBox.style.display = "block"  
    }else{
        msgBox.style.display = "none"
    }
}

// myInput.onblur = function() {
//   msgBox.style.display = "none";
//   reqButton.style.display = "none";
// }

myInput.onkeyup = function() {
  const lowerCaseLetters = /[a-z]/g;

  if(length.classList.contains("valid") && letter.classList.contains("valid") && capital.classList.contains("valid") && number.classList.contains("valid")){
    reqButton.style.display = "none";
  }
  else{
    reqButton.style.display = "block";
  }

  
  if(myInput.value.match(lowerCaseLetters)) {  
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
  }
  
  // Validate capital letters
  const upperCaseLetters = /[A-Z]/g;
  if(myInput.value.match(upperCaseLetters)) {  
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  // Validate numbers
  const numbers = /[0-9]/g;
  if(myInput.value.match(numbers)) {  
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }
  
  // Validate length
  if(myInput.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
}