//Start update proprietario script
function clickUpdateCorretor(id) {
    $('#modal-alterar-corretor').attr('id_corretor', id);
    var url_corretor = $(location).attr('href').replace("/corretores", "/atualizar_view_corretor/" + id);
    console.log(url_corretor);
    $.get(url_corretor, function (data) {
        $('input#nome').val(data["nome"]);
        $('input#cpf-alterar').val(data["cpf"]);
        $('input#rg').val(data["rg"]);
        $('input#creci').val(data["creci"]);
        $('input#endereco').val(data["endereco"]);
        $('input#bairro').val(data["bairro"]);
        $('input#cidade').val(data["cidade"]);
        $('input#cep').val(data["cep"]);
        $('input#uf').val(data["uf"]);
        $('input#email').val(data["email"]);
        $('input#tel').val(data["telefone"]);
    });
};

$("#btn-atualizar-corretor").on("click", function () {
    console.log("botao atualizar acionado");
    var id = $('#modal-alterar-corretor').attr("id_corretor");
    var href_alterar = $(location).attr("href").replace('cadastro/corretores', 'api/corretor/' + id);
    var url_alterar = href_alterar.slice(0, -1);

    var nome = $('input#nome').val();
    var cpf = $('input#cpf-alterar').val();
    var rg = $('input#rg').val();
    var creci = $('input#creci').val();
    var endereco = $('input#endereco').val();
    var bairro = $('input#bairro').val();
    var cidade = $('input#cidade').val();
    var cep = $('input#cep').val();
    var uf = $('input#uf').val();
    var email = $('input#email').val();
    var telefone = $('input#tel').val();

    var url_token = $(location).attr("href").replace('cadastro/corretores', 'api/token');
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
        "creci": creci,
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


//Start delete corretor script//
function clickDeleteCorretor(id) {
    $('#modal-exluir-corretor').attr('id_corretor', id);
};

$("#btn-delete-corretor").on("click", function () {
    var id = $('#modal-exluir-corretor').attr("id_corretor");
    var href_excluir = $(location).attr("href").replace('/corretores', '/delete_corretor/' + id);
    $(location).attr("href", href_excluir);
});
//End delete corretor script//