const title = document.querySelector("title").text;

if (title.trim() == "Home | Nominator"){
    document.querySelector('#clickid1').classList.toggle("active");
}

if (title.trim() == "Home | About"){
    document.querySelector('#clickid2').classList.toggle("active");
}

if (title.trim() == "Tests"){
    document.querySelector('#clickid3').classList.toggle("active");
}

if (title.trim()=="Home | Company"){
    document.querySelector('#clickid4').classList.toggle("active")
}

if (title.trim()=="Home | Login"){
    document.querySelector('#clickid5').classList.toggle("active")
}

function changeNav() {
    document.querySelector(".nav-ham").classList.toggle("change");
    document.querySelector(".menu-bg").classList.toggle("change-bg");
    document.querySelector(".main-nav").classList.toggle("change");
  }
  
function showDropdown(){
    document.querySelector(".dropdown-profile").classList.toggle("show");
}

window.onclick = function(event) {
    const openDropdown = document.querySelector(".dropdown-profile")
    if (!event.target.matches('.btn-profile') && !event.target.matches('.dropdown-content')  && openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
    } 
  }