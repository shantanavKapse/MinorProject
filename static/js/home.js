document.getElementById('heading').addEventListener('click', function onClick(event){
    if (document.getElementById('heading').style.color == 'red'){
        document.getElementById('heading').style.color = 'green';
    }
    else{
        document.getElementById('heading').style.color = 'red';
    }
});