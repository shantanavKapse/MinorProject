const title = document.querySelector("title").text;

if (title.trim() == "Home|Nominator"){
    document.querySelector('#clickid1').classList.toggle("active");
}

if (title.trim() == "Home|About"){
    document.querySelector('#clickid2').classList.toggle("active");
}

function changeNav() {
    document.querySelector(".nav-ham").classList.toggle("change");
    document.querySelector(".menu-bg").classList.toggle("change-bg");
    document.querySelector(".main-nav").classList.toggle("change");
  }