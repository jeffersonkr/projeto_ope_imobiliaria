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