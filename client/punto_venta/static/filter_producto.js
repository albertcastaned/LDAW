$(document).ready(function(){
    $("#inventario-input").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#inventario-table-body tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });