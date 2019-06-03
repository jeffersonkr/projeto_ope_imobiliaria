//Start update imovel script
function clickUpdateImovel(id) {
    $('#modal-alterar-imovel').attr('id_imovel', id);
    var url_imovel = $(location).attr('href').replace("/imoveis", "/atualizar_view_imovel/" + id);
    $.get(url_imovel, function (data) {
        $('input#matricula').val(data["matricula"]);
        $('textarea#descricao').val(data["descricao"]);
        $('input#iptu').val(data["iptu"]);
        $('select#id_proprietario').val(data["id_proprietario"]);
        $('select#id_corretor').val(data["id_corretor"]);
        $('input#sabesp').val(data["n_sabesp"]);
        $('input#eletropaulo').val(data["n_eletropaulo"]);
        $('input#valor_aluguel').val(data["valor_aluguel"]);
        $('input#valor_venda').val(data["valor_venda"]);
        $('input#metro_quadrado').val(data["metragem"]);
        $('select#servico').val(data["tipo_servico"]);
        $('select#status').val(data["status_imovel"]);
        $('input#latitude').val(data["latitude"]);
        $('input#longitude').val(data["longitude"]);
        $('input#endereco').val(data["endereco"]);
        $('input#bairro').val(data["bairro"]);
        $('input#cidade').val(data["cidade"]);
        $('input#cep').val(data["cep"]);
        $('input#uf').val(data["uf"]);
        $('input#photo1').val(data["imagem_1"]);
        $('input#photo2').val(data["imagem_2"]);
        $('input#photo3').val(data["imagem_3"]);
        $('input#photo4').val(data["imagem_4"]);
        $('input#photo5').val(data["imagem_5"]);
        if (data["residencial"] == true) {
            $("#residencial").prop("checked", true);
        } else {
            $("#residencial").prop("checked", false);
        }
    });
};


$("#btn-atualizar-imovel").on("click", function () {
    console.log("botao atualizar acionado");
    var id = $('#modal-alterar-imovel').attr("id_imovel");
    var href_alterar = $(location).attr("href").replace('cadastro/imoveis', 'api/imovel/' + id);
    var url_alterar = href_alterar.slice(0, -1);
    var matricula = $('input#matricula').val();
    var descricao = $('textarea#descricao').val();
    var valor_aluguel = $('input#valor_aluguel').val();
    var valor_venda = $('input#valor_venda').val();
    var iptu = $('input#iptu').val();
    var id_proprietario = $('select#id_proprietario').val();
    var id_corretor = $('select#id_corretor').val();
    var n_sabesp = $('input#sabesp').val();
    var n_eletropaulo = $('input#eletropaulo').val();
    var metragem = $('input#metro_quadrado').val();
    var tipo_servico = $('select#servico').val();
    var status_imovel = $('select#status').val();
    var latitude = $('input#latitude').val();
    var longitude = $('input#longitude').val();
    var endereco = $('input#endereco').val();
    var bairro = $('input#bairro').val();
    var cidade = $('input#cidade').val();
    var cep = $('input#cep').val();
    var uf = $('input#uf').val();
    var imagem_1 = $('input#photo1').val();
    var imagem_2 = $('input#photo2').val();
    var imagem_3 = $('input#photo3').val();
    var imagem_4 = $('input#photo4').val();
    var imagem_5 = $('input#photo5').val();
    var residencial = $("#residencial").is(":checked");

    var url_token = $(location).attr("href").replace('cadastro/imoveis', 'api/token');
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
        "matricula": matricula,
        "descricao": descricao,
        "iptu": iptu,
        "id_proprietario": id_proprietario,
        "id_corretor": id_corretor,
        "n_sabesp": n_sabesp,
        "n_eletropaulo": n_eletropaulo,
        "valor_aluguel": valor_aluguel,
        "valor_venda": valor_venda,
        "metragem": metragem,
        "tipo_servico": tipo_servico,
        "status_imovel": status_imovel,
        "residencial": residencial,
        "latitude": latitude,
        "longitude": longitude,
        "imagem_1": imagem_1,
        "imagem_2": imagem_2,
        "imagem_3": imagem_3,
        "imagem_4": imagem_4,
        "imagem_5": imagem_5,
        "endereco": endereco,
        "bairro": bairro,
        "cidade": cidade,
        "cep": cep,
        "uf": uf,
    };
    console.log(data_atualizado);
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



//Start delete imovel script//
function clickDeleteImovel(id) {
    $('#modal-excluir-imovel').attr('id_imovel', id);
};

$("#btn-delete-imovel").on("click", function () {
    var id = $('#modal-excluir-imovel').attr("id_imovel");
    var href_excluir = $(location).attr("href").replace('/imoveis', '/delete_imovel/' + id);
    $(location).attr("href", href_excluir);
});
//End delete cliente script//