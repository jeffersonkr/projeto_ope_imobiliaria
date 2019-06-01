$(document).ready(function () {
    $('#pj').click(function () {
        if ($(this).prop("checked") == true) {
            $('#cnpj').prop("disabled", false);
        } else if ($(this).prop("checked") == false) {
            $('#cnpj').prop("disabled", true);
        }
    });
});