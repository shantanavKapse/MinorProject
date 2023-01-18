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

