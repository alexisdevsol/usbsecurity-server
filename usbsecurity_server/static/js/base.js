$(document).ready(function() {
    $('.toggle-vis-psw').click(function () {
        let target = $(this).data('target');
        let icon = $(this).find('.mdi');
        let inputPsw = $('#'+target);
        let inputPswSee = inputPsw.data('see');

        if (inputPswSee === 'off') {
            inputPsw.find('input').attr('type', 'text');
            inputPsw.data('see', 'on');
            icon.removeClass('mdi-eye-outline');
            icon.addClass('mdi-eye-off-outline');
        } else {
            inputPsw.find('input').attr('type', 'password');
            inputPsw.data('see', 'off');
            icon.removeClass('mdi-eye-off-outline');
            icon.addClass('mdi-eye-outline');
        }
    });
});
