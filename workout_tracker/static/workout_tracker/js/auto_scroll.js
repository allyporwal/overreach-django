$('.scroll-icon').click(function() {
    $(this).parent().animate({ scrollTop: $(this).parent().height() }, 325);
})

$('.scroll-icon-up').click(function() {
    $(this).parent().animate({ scrollTop: -$(this).parent().height() }, 325);
})