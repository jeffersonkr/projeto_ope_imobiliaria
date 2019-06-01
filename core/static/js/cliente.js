//Start update cliente script
function clickUpdate(id) {
    $('#modal-alterar-cliente').attr('id_cliente', id);
    var url_cliente = $(location).attr('href').replace("/clientes", "/atualizar_view_cliente/" + id);
    $.get(url_cliente, function (data) {
        console.log(data);
        $('input#nome').val(data["nome"]);
        $('input#cpf-alterar').val(data["cpf"]);
        $('input#rg').val(data["rg"]);
        $('input#cnpj_alt').val(data["cnpj"]);
        $('input#endereco').val(data["endereco"]);
        $('input#bairro').val(data["bairro"]);
        $('input#cidade').val(data["cidade"]);
        $('input#cep').val(data["cep"]);
        $('input#uf').val(data["uf"]);
        $('input#email').val(data["email"]);
        $('input#tel').val(data["telefone"]);
        if (data["pessoa_juridica"] == true) {
            $("#pj_alt").prop("checked", true);
        } else {
            $("#pj_alt").prop("checked", false);
        }
        if (data["inquilino"] == true) {
            $("#inquilino_alt").prop("checked", true);
        } else {
            $("#inquilino_alt").prop("checked", false);
        }
    });
};


$("#btn-atualizar-cliente").on("click", function () {
    console.log("botao atualizar acionado");
    var id = $('#modal-alterar-cliente').attr("id_cliente");
    var href_alterar = $(location).attr("href").replace('cadastro/clientes', 'api/cliente/' + id);
    var url_alterar = href_alterar.slice(0, -1);

    var nome = $('input#nome').val();
    var cpf = $('input#cpf-alterar').val();
    var rg = $('input#rg').val();
    var cnpj = $('input#cnpj_alt').val();
    var pj = $("#pj_alt").is(":checked");
    var inquilino = $("#inquilino_alt").is(":checked");
    var endereco = $('input#endereco').val();
    var bairro = $('input#bairro').val();
    var cidade = $('input#cidade').val();
    var cep = $('input#cep').val();
    var uf = $('input#uf').val();
    var email = $('input#email').val();
    var telefone = $('input#tel').val();

    var url_token = $(location).attr("href").replace('cadastro/clientes', 'api/token');
    $.ajax({
        url: url_token,
        type: 'POST',
        dataType: 'json',
        data: {
            grant_type: 'password',
            username: "admin",
            password: "admin"
        },
        success: function (data) {
            localStorage.setItem('token', data['access']);
        }
    });

    var token = localStorage.getItem('token');
    var headers = { 'Authorization': 'Bearer ' + token };

    var data_atualizado = {
        "nome": nome,
        "cpf": cpf,
        "rg": rg,
        "cnpj": cnpj,
        "inquilino": inquilino,
        "pessoa_juridica": pj,
        "endereco": endereco,
        "bairro": bairro,
        "cidade": cidade,
        "cep": cep,
        "uf": uf,
        "email": email,
        "telefone": telefone,
    };

    $.ajax({
        url: url_alterar,
        type: 'PUT',
        data: data_atualizado,
        headers: headers,
        dataType: 'json',
        success: function (data) {
            alert('Alterado com sucesso.');
            $(location).attr("href", $(location).attr("href"));
        },
        error: function (result) {
            console.log(result);
        }
    });
});

//Start delete cliente script//
function clickDelete(id) {
    $('#modal-exluir-cliente').attr('id_cliente', id);
};

$("#btn-delete-cliente").on("click", function () {
    var id = $('#modal-exluir-cliente').attr("id_cliente");
    var href_excluir = $(location).attr("href").replace('/clientes', '/delete_cliente/' + id);
    $(location).attr("href", href_excluir);
});
//End delete cliente script//
