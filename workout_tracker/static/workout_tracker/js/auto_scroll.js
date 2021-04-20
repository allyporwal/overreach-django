$('.scroll-icon').click(function() {
    $(this).parent().animate({ scrollTop: $(document).height() }, 1000);
})

$('.scroll-icon-up').click(function() {
    $(this).parent().animate({ scrollTop: -$(document).height() }, 1000);
})