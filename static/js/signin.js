$('#signup').click(function() {
    $('.movebox').css('transform', 'translateX(90%)');
    $('.signin').addClass('nodisplay');
    $('.signup').removeClass('nodisplay');
});

$('#signin').click(function() {
    $('.movebox').css('transform', 'translateX(-3%)');
    $('.signup').addClass('nodisplay');
    $('.signin').removeClass('nodisplay');
});