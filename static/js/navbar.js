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
    const dropdown = document.querySelector(".dropdown-profile");
    if(dropdown.style.display == "none"){
        dropdown.style.display = "block";
    }
    else{
        dropdown.style.display = "none";
    }
}