$("#clickid1,#clickid2,#clickid3,#clickid4,#clickid5").click(function(){
    $('.active').classList.remove('active');
    $(this).classList.add('active');
});

