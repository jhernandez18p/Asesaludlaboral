$(document).ready(function(){
    $(function(){
        var menu = $("#myMenu");
        $(window).scroll(function(){
            var scroll = $(window).scrollTop();
            if (scroll >= 80){
                if(!menu.hasClass("fixedMenu")){
                    menu.addClass('fixedMenu').fadeIn(1000);
                }
            } else {
                if(menu.hasClass("fixedMenu")){
                    menu.removeClass("fixedMenu").fadeIn(1000);
                }
            }
        });
    });
});
