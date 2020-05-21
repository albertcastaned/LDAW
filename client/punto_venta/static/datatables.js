$(document).ready(function() {
    $('.table').DataTable({
        autoWidth: false,
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