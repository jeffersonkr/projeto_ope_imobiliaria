$(document).ready(function () {
    $('input[type=checkbox]#pessoa_juridica_true').click(function () {
        if ($(this).prop("checked") == true) {
            $('#cnpj').prop("disabled", false);
        } else if ($(this).prop("checked") == false) {
            $('#cnpj').prop("disabled", true);
        }
    });
});