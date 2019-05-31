$(function () {
    $('#cpf-incluir').blur(function () {
        var cpf = $('#cpf-incluir').val().replace(/[^0-9]/g, '').toString();
        if (cpf.length == 11) {
            var v = [];

            //Calcula o primeiro dígito de verificação.
            v[0] = 1 * cpf[0] + 2 * cpf[1] + 3 * cpf[2];
            v[0] += 4 * cpf[3] + 5 * cpf[4] + 6 * cpf[5];
            v[0] += 7 * cpf[6] + 8 * cpf[7] + 9 * cpf[8];
            v[0] = v[0] % 11;
            v[0] = v[0] % 10;

            //Calcula o segundo dígito de verificação.
            v[1] = 1 * cpf[1] + 2 * cpf[2] + 3 * cpf[3];
            v[1] += 4 * cpf[4] + 5 * cpf[5] + 6 * cpf[6];
            v[1] += 7 * cpf[7] + 8 * cpf[8] + 9 * v[0];
            v[1] = v[1] % 11;
            v[1] = v[1] % 10;

            //Retorna Verdadeiro se os dígitos de verificação são os esperados.
            if ((v[0] != cpf[9]) || (v[1] != cpf[10])) {
                $("#cpf-error-incluir").css({
                    "color": "rgba(163, 5, 5, 0.966)",
                    "font-size": "12px",
                    "text-align": "center",
                    "padding-bottom": "8px"
                });
                $("#btn-cad-cliente").css({ "display": "none" });
                $("#cpf-error-incluir").html("Digite um CPF válido!");
                $('#cpf-incluir').val('');
                $('#cpf-incluir').focus();
            } else {
                $("#btn-cad-cliente").css({ "display": "inline-block" });
                $("#cpf-error-incluir").html("");
            }
        } else {
            $("#cpf-error-incluir").css({
                "color": "rgba(163, 5, 5, 0.966)",
                "font-size": "12px",
                "text-align": "center",
                "padding-bottom": "8px"
            });
            $("#btn-cad-cliente").css({ "display": "none" });
            $("#cpf-error-incluir").html("Digite um CPF válido!");
            $('#cpf-incluir').val('');
            $('#cpf-incluir').focus();
        }
    });
});


$(function () {
    $('#cpf-alterar').blur(function () {
        var cpf = $('#cpf-alterar').val().replace(/[^0-9]/g, '').toString();
        if (cpf.length == 11) {
            var v = [];

            //Calcula o primeiro dígito de verificação.
            v[0] = 1 * cpf[0] + 2 * cpf[1] + 3 * cpf[2];
            v[0] += 4 * cpf[3] + 5 * cpf[4] + 6 * cpf[5];
            v[0] += 7 * cpf[6] + 8 * cpf[7] + 9 * cpf[8];
            v[0] = v[0] % 11;
            v[0] = v[0] % 10;

            //Calcula o segundo dígito de verificação.
            v[1] = 1 * cpf[1] + 2 * cpf[2] + 3 * cpf[3];
            v[1] += 4 * cpf[4] + 5 * cpf[5] + 6 * cpf[6];
            v[1] += 7 * cpf[7] + 8 * cpf[8] + 9 * v[0];
            v[1] = v[1] % 11;
            v[1] = v[1] % 10;

            //Retorna Verdadeiro se os dígitos de verificação são os esperados.
            if ((v[0] != cpf[9]) || (v[1] != cpf[10])) {
                $("#cpf-error-alterar").css({
                    "color": "rgba(163, 5, 5, 0.966)",
                    "font-size": "12px",
                    "text-align": "center",
                    "padding-bottom": "8px"
                });
                $("#btn-atualizar-cliente").css({ "display": "none" });
                $("#cpf-error-alterar").html("Digite um CPF válido!");

                $('#cpf-alterar').val('');
                $('#cpf-alterar').focus();
            } else {
                $("#btn-atualizar-cliente").css({ "display": "inline-block" });
                $("#cpf-error-alterar").html("");
            }
        } else {
            $("#cpf-error-alterar").css({
                "color": "rgba(163, 5, 5, 0.966)",
                "font-size": "12px",
                "text-align": "center",
                "padding-bottom": "8px"
            });
            $("#btn-atualizar-cliente").css({ "display": "none" });
            $("#cpf-error-alterar").html("Digite um CPF válido!");

            $('#cpf-alterar').val('');
            $('#cpf-alterar').focus();
        }
    });
});