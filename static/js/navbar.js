const title = document.querySelector("title").text;

if (title.trim() == "Home|Nominator"){
    document.querySelector('#clickid1').querySelector('a').classList.add("active");
}