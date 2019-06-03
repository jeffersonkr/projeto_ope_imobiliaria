//Start update imovel script
function clickUpdateImovel(id) {
    $('#modal-alterar-imovel').attr('id_imovel', id);
    var url_imovel = $(location).attr('href').replace("/imoveis", "/atualizar_view_imovel/" + id);
    $.get(url_imovel, function (data) {
        $('input#matricula').val(data["matricula"]);
        $('textarea#descricao').val(data["descricao"]);
        $('input#iptu').val(data["iptu"]);
        $('input#metro_quadrado').val(data["metro_quadrado"]);
        $('select#id_proprietario').val(data["id_proprietario"]);
        $('select#id_cliente').val(data["id_cliente"]);
        $('input#endereco').val(data["endereco"]);
        $('input#bairro').val(data["bairro"]);
        $('input#cidade').val(data["cidade"]);
        $('input#cep').val(data["cep"]);
        $('input#uf').val(data["uf"]);
    });
};


$("#btn-atualizar-imovel").on("click", function () {
    var id = $('#modal-alterar-imovel').attr("id_imovel");
    var href_alterar = $(location).attr("href").replace('cadastro/imoveis', 'api/imovel/' + id);
    var url_alterar = href_alterar.slice(0, -1);
    var matricula = $('input#matricula').val();
    var descricao = $('textarea#descricao').val();
    var iptu = $('input#iptu').val();
    var metro_quadrado = $('input#metro_quadrado').val();
    var id_proprietario = $('select#id_proprietario').val();
    var id_cliente = $('select#id_cliente').val();
    var endereco = $('input#endereco').val();
    var bairro = $('input#bairro').val();
    var cidade = $('input#cidade').val();
    var cep = $('input#cep').val();
    var uf = $('input#uf').val();

    $.ajax({
        url: url_alterar,
        type: 'PUT',
        data: JSON.stringify({
            "id": id,
            "matricula": matricula,
            "descricao": descricao,
            "iptu": iptu,
            "metro_quadrado": metro_quadrado,
            "id_proprietario": id_proprietario,
            "id_cliente": id_cliente,
            "endereco": endereco,
            "bairro": bairro,
            "cidade": cidade,
            "cep": cep,
            "uf": uf,
        }),
        dataType: 'json',
        success: function (data) {
            alert('Alterado com sucesso.');
            $(location).attr("href", $(location).attr("href"));
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



$('#photo1').on('change', function () {
    var fileName = document.getElementById('label_photo1');
    var photo_name = this.value;
    photo_name = photo_name.split("\\").slice(-1);
    fileName.textContent = photo_name;
})

$('#photo2').on('change', function () {
    var fileName = document.getElementById('label_photo2');
    var photo_name = this.value;
    photo_name = photo_name.split("\\").slice(-1);
    fileName.textContent = photo_name;
})

$('#photo3').on('change', function () {
    var fileName = document.getElementById('label_photo3');
    var photo_name = this.value;
    photo_name = photo_name.split("\\").slice(-1);
    fileName.textContent = photo_name;
})

$('#photo4').on('change', function () {
    var fileName = document.getElementById('label_photo4');
    var photo_name = this.value;
    photo_name = photo_name.split("\\").slice(-1);
    fileName.textContent = photo_name;
})

$('#photo5').on('change', function () {
    var fileName = document.getElementById('label_photo5');
    var photo_name = this.value;
    photo_name = photo_name.split("\\").slice(-1);
    fileName.textContent = photo_name;
})