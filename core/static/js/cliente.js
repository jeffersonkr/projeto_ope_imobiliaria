//Start update cliente script
function clickUpdate(id) {
    $('#modal-alterar-cliente').attr('id_cliente', id);
    var url_cliente = $(location).attr('href').replace("/clientes", "/atualizar_view_cliente/" + id);
    $.get(url_cliente, function (data) {
        console.log(data);
        $('input#nome').val(data["nome_cliente"]);
        $('input#cpf-alterar').val(data["cpf_cnpj"]);
        $('input#endereco').val(data["endereco"]);
        $('input#bairro').val(data["bairro"]);
        $('input#cidade').val(data["cidade"]);
        $('input#cep').val(data["cep"]);
        $('input#uf').val(data["uf"]);
        $('input#email').val(data["email"]);
        $('input#tel').val(data["telefone"]);
    });
};


$("#btn-atualizar-cliente").on("click", function () {
    console.log("botao atualizar acionado");
    var id = $('#modal-alterar-cliente').attr("id_cliente");
    var href_alterar = $(location).attr("href").replace('cadastro/clientes', 'api/cliente/' + id);
    var url_alterar = href_alterar.slice(0, -1);
    var nome = $('input#nome').val();
    var cpf_cnpj = $('input#cpf-alterar').val();
    var endereco = $('input#endereco').val();
    var bairro = $('input#bairro').val();
    var cidade = $('input#cidade').val();
    var cep = $('input#cep').val();
    var uf = $('input#uf').val();
    var email = $('input#email').val();
    var telefone = $('input#tel').val();

    $.ajax({
        url: url_alterar,
        type: 'PUT',
        data: JSON.stringify({
            "id": id,
            "nome_cliente": nome,
            "cpf_cnpj": cpf_cnpj,
            "endereco": endereco,
            "bairro": bairro,
            "cidade": cidade,
            "cep": cep,
            "uf": uf,
            "email": email,
            "telefone": telefone
        }),
        dataType: 'json',
        success: function (data) {
            alert('Alterado com sucesso.');
            $(location).attr("href", $(location).attr("href"));
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
