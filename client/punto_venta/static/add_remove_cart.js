$(document).ready(function(){
    function updateTotal() {
        var total = 0;
        $('input[name=total]').each(function(index, el) {
            total += parseFloat(el.value);
         });
         $("#cart-total").text(parseFloat(total).toFixed(2));
         check_valid();
    }

    function check_valid()
    {
        total = parseFloat($("#cart-total").text()).toFixed(2);
        if(total <= 0)
        {
            $('#submit').prop("disabled", true);
        }else{
            $('#submit').prop("disabled", false);

        }
    }

    function validateQuantity(){
        


    }

    $("#inventario-table-body").on("click", '.add-cart-compra', function() {

        row = $(this).closest("tr");
        tds = row.find("td");

        id = row.find("td:nth-child(1)").text();
        nombre = row.find("td:nth-child(2)").text();
        precio_Compra = parseFloat(row.find("td:nth-child(4)").text()).toFixed(2);


        form_input_head = `
        <div class="row">`;

        form_input_id = `
        <div class="form-group col-md-1">
        <label class="form-control-label" for="id">ID</label>
        <input readonly name="id[]" type="number" value="${id}" class="form-control form-control-lg" >
        </div>
        `
        ;

        form_input_nombre = `
        <div class="form-group col-md-3">
        <label class="form-control-label" for="nombre">Nombre</label>
        <input readonly name="nombre[]" type="text" value="${nombre}" class="form-control form-control-lg">
        </div>
        `;
        
        form_input_precioCompra = `
        <div class="form-group col-md-2">
        <label class="form-control-label" for="precioCompra">Precio de Compra</label>
        <input name="precioCompra[]" min="0.01" step=".01" type="number" value="${precio_Compra}" class="form-control form-control-lg price-definer precio">
        </div>
        `;
        
        form_input_cantidad = `
        <div class="form-group col-md-2">
        <label class="form-control-label" for="cantidad">Cantidad</label>
        <input name="cantidad[]" type="number" min="0" value="1" class="form-control form-control-lg price-definer cantidad">
        </div>
        `;

        form_input_total = `
        <div class="form-group col-md-2">
        <label class="form-control-label" for="total">Subtotal</label>
        <input disabled name="total" type="number" value="${precio_Compra}" class="form-control form-control-lg total">
        </div>
        `;

        form_input_eliminar = `
        <div class="col-md-2 form-inline">
        <button type="button" class="btn btn-danger btn-sm remove-cart">Eliminar</button>
        </div>
        `;

        form_input_bottom = `</div>`;

        form_input = form_input_head + form_input_id + form_input_nombre + form_input_precioCompra + form_input_cantidad  + form_input_total + form_input_eliminar+ form_input_bottom; 
        $(`#cart`).append(form_input);
        updateTotal();

    });

    $("#inventario-venta-table-body").on("click", '.add-cart-venta', function() {
        row = $(this).closest("tr");
        tds = row.find("td");

        id = row.find("td:nth-child(1)").text();
        nombre = row.find("td:nth-child(2)").text();
        precio_Venta = parseFloat(row.find("td:nth-child(3)").text()).toFixed(2);


        cantidad = parseFloat(row.find("td:nth-child(5)").text()).toFixed(2);


        form_input_head = `
        <div class="row">`;

        form_input_id = `
        <div class="form-group col-md-1">
        <label class="form-control-label" for="id">ID</label>
        <input readonly name="id[]" type="number" value="${id}" class="form-control form-control-lg" >
        </div>
        `
        ;

        form_input_nombre = `
        <div class="form-group col-md-3">
        <label class="form-control-label" for="nombre">Nombre</label>
        <input readonly name="nombre[]" type="text" value="${nombre}" class="form-control form-control-lg">
        </div>
        `;
        
        form_input_precioVenta = `
        <div class="form-group col-md-2">
        <label class="form-control-label" for="precioVentaBase">Precio de Venta</label>
        <input name="precioVenta[]" min="0.01" step=".01" type="number" value="${precio_Venta}" class="form-control form-control-lg price-definer precio">
        </div>
        `;
        
        form_input_cantidad = `
        <div class="form-group col-md-2">
        <label class="form-control-label" for="cantidad">Cantidad</label>
        <input name="cantidad[]" type="number" min="0" max="${cantidad}" value="1" class="form-control form-control-lg price-definer cantidad">
        </div>
        `;
        console.log(cantidad);
        form_input_total = `
        <div class="form-group col-md-2">
        <label class="form-control-label" for="total">Subtotal</label>
        <input disabled name="total" type="number" value="${precio_Venta}" class="form-control form-control-lg total">
        </div>
        `;

        form_input_eliminar = `
        <div class="col-md-2 form-inline">
        <button type="button" class="btn btn-danger btn-sm remove-cart">Eliminar</button>
        </div>
        `;

        form_input_bottom = `</div>`;

        form_input = form_input_head + form_input_id + form_input_nombre + form_input_precioVenta + form_input_cantidad  + form_input_total + form_input_eliminar+ form_input_bottom; 
        $(`#cart`).append(form_input);
        updateTotal();

 
    });


    $("#cart").on("click", '.remove-cart', function(e) {
        $(this).closest("div.row").remove();
        e.preventDefault();
        updateTotal();

    });


    $('#cart').on("keyup change", '.price-definer', function(e){
        precio = $(this).parent().parent().find(".precio").val();
        if(precio == '' || parseFloat(precio) < 0)
            precio = 0;
        cantidad = $(this).parent().parent().find(".cantidad").val();
        if(cantidad == '' || parseFloat(cantidad) < 0)
            cantidad = 0;
        total = $(this).parent().parent().find(".total");

        total.val((parseFloat(precio) * parseFloat(cantidad)).toFixed(2));
        
        e.preventDefault();
        updateTotal();

    });
  });