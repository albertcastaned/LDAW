$(".alert").slideDown().delay( 300 );
$(".alert button.close").click(function (e) {
    $(this).parent().fadeOut('medium');
});