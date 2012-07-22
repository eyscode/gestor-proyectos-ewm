$(document).ready(function () {
    $('#dock .option').mouseenter(function () {
        $(this).children().css('background-color', '#5D9AB9');
        var clase = $(this).find('.icono').attr('class').split(" ")[0];
        $(this).find('.icono').css('background', 'no-repeat url("../static/img/dock/' + clase + '_go.png")');
    });
    $('#dock .option').mouseleave(function () {
        $(this).children().css('background-color', '#2D6987');
        var clase = $(this).find('.icono').attr('class').split(" ")[0];
        $(this).find('.icono').css('background', 'no-repeat url("../static/img/dock/' + clase + '.png")');
    });
    setInterval(function () {
        if ($(window).height() <= 600) {
            console.log("ptm");
            if ($(window).scrollTop() <= 103) {
                $('#dock').css('position', 'absolute');
            } else {
                $('#dock').css('position', 'fixed');
            }
        } else {
            $('#dock').css('position', 'fixed');
        }
    }, 100);
});