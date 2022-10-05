$("#clickid,#clickid1,#clickid2,#clickid4,#clickid5").click(function(){
    $('.active').removeClass('active');
    $(this).addClass('active');
});