
//Start update proprietario script
function clickUpdateProprietario(id) {
    $('#modal-alterar-proprietario').attr('id_proprietario', id);
    var url_cliente = $(location).attr('href').replace("/proprietarios", "/atualizar_view_proprietario/" + id);
    $.get(url_cliente, function (data) {
        console.log(data);
        $('input#nome').val(data["nome_proprietario"]);
        $('input#cpf-alterar').val(data["cpf"]);
        $('input#endereco').val(data["endereco"]);
        $('input#bairro').val(data["bairro"]);
        $('input#cidade').val(data["cidade"]);
        $('input#cep').val(data["cep"]);
        $('input#uf').val(data["uf"]);
        $('input#email').val(data["email"]);
        $('input#tel').val(data["telefone"]);
    });
};

$("#btn-atualizar-proprietario").on("click", function () {
    console.log("botao atualizar acionado");
    var id = $('#modal-alterar-proprietario').attr("id_proprietario");
    var href_alterar = $(location).attr("href").replace('cadastro/proprietarios', 'api/proprietario/' + id);
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
            "nome_proprietario": nome,
            "cpf": cpf_cnpj,
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


//Start delete proprietario script//
function clickDeleteProprietario(id) {
    $('#modal-excluir-proprietario').attr('id_proprietario', id);
};

$("#btn-delete-proprietario").on("click", function () {
    var id = $('#modal-excluir-proprietario').attr("id_proprietario");
    var href_excluir = $(location).attr("href").replace('/proprietarios', '/delete_proprietario/' + id);
    $(location).attr("href", href_excluir);
});
//End delete cliente script//