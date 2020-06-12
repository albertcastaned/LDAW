$(document).ready(function() {
    var table = $('.table').DataTable({
        order: [],
        pageLength: 15,
        autoWidth: false,
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'pdf',
                text: 'Descargar PDF'
            },
            {
                extend: 'print',
                text: 'Imprimir'
            },
            {
                text: 'Enviar Correo',
                action: function(e, dt, node, conf) {

                    var data = dt.buttons.exportData();
                    $.ajax({
                        type: 'POST',
                        url: "/correo",
                        data: JSON.stringify(data),
                        contentType: 'application/json',
                        success: function(data){
                            alert("Se envio el correo exitosamente (Verificar en Correo No Deseado si no aparece)");
                            }
                      });
                }
            }
        ],
        "language": {
            "lengthMenu": "Mostrar _MENU_ registros por pagina",
            "search": "Buscar",
            "zeroRecords": "No hay registros existentes",
            "infoEmpty": "No encontramos registros con dichas caracteristicas",
            "info": "Enseñando _PAGE_ de _PAGES_ paginas",
            "loadingRecords": "Cargando...",
            "infoFiltered":   "(filtrado de _MAX_ registros totales)",
            "paginate":{
                "first":"Primero",
                "previous":"Anterior",
                "next":"Siguiente",
                "last":"Ultimo"
            },
            "aria": {
                "sortAscending":  ": activar para ordenar columna en orden ascendiente",
                "sortDescending": ": activar para ordenar columna en orden descendiente"
            }
        },

    });
} );