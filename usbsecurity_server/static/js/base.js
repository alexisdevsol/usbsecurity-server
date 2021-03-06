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

    $('.url-to-clipboard').click(function () {
        const url = window.location.href.split("?");
        copyToClipboard(url);
        bulmaToast.toast({
            message: gettext('Link copied to clipboard'),
            type: 'is-light',
            position: 'bottom-center',
            duration: 3000,
            dismissible: true,
            pauseOnHover: true,
        });
    });
});

function copyToClipboard(text) {
  let aux = document.createElement('input');
  aux.setAttribute('value', text);
  document.body.appendChild(aux);
  aux.select();
  document.execCommand('copy');
  document.body.removeChild(aux);
}
