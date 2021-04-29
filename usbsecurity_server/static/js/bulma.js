$(document).ready(function() {
    $('.navbar-burger').click(function () {
        const target = $(this).data('target');
        $('#'+target).slideToggle('is-active');
    });

    $('.button-modal').click(function () {
        const target = $(this).data('target');
        $('#'+target).addClass('is-active');
    });

    $('.modal-close').click(function () {
        const target = $(this).parents('.modal')[0];
        $(target).removeClass('is-active');
    });

    $('.delete').click(function () {
        const target = $(this).parents('.modal')[0];
        $(target).removeClass('is-active');
    });

    $('.cancel').click(function () {
        const target = $(this).parents('.modal')[0];
        $(target).removeClass('is-active');
    });

    $('.modal-background').click(function () {
        const target = $(this).parents('.modal')[0];
        $(target).removeClass('is-active');
    });

    $(document).keydown(function (e) {
        if (e.keyCode === 27) {
            $('.modal').removeClass('is-active');
        }
    });
});