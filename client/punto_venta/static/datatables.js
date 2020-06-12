$(document).ready(function() {
    $('.table').DataTable({
        order: [],
        pageLength: 15,
        autoWidth: false,
        dom: 'Bfrtip',
        buttons: [
            'pdf'
        ],
        "language": {
            "lengthMenu": "Mostrar _MENU_ registros por página",
            "search": "Buscar",
            "zeroRecords": "No hay registros existentes",
            "infoEmpty": "No encontramos registros con dichas características",
            "info": "Mostrando _PAGE_ de _PAGES_ paginas",
            "loadingRecords": "Cargando...",
            "infoFiltered":   "(filtrado de _MAX_ registros totales)",
            "paginate":{
                "first":"Primero",
                "previous":"Anterior",
                "next":"Siguiente",
                "last":"Último"
            },
            "aria": {
                "sortAscending":  ": activar para ordenar columna en orden ascendiente",
                "sortDescending": ": activar para ordenar columna en orden descendiente"
            }
        },

    });
} );