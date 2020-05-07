from flask import render_template, url_for, flash, redirect, request, Blueprint
from punto_venta.productos.forms import *
import requests, json
from punto_venta import API_URL
from punto_venta.utils import login_required

productos = Blueprint('productos', __name__, template_folder='templates')


@productos.route("/productos/registrar", methods=['GET', 'POST'])
@login_required
def registrar_producto():
    form = RegistarProductoForm()
    if form.validate_on_submit():
        post_data = {
            'nombre_producto':form.nombre_producto.data,
            'descripcion':form.descripcion_producto.data,
            'marca':form.marca_producto.data,
            'precioVentaBase':str(form.precio_venta.data),
            'precioCompra':str(form.precio_compra.data),
            'proveedor':form.proveedor.data
        }
        response = requests.post(API_URL + "productos/registrar", json = post_data)

        if(response.status_code == 200 or response.status_code == 201):
            flash('El producto a sido registrado exitosamente', 'success')
            return redirect(url_for('productos.productos_lista'))
        else:
            if(response.status_code == 501):
                flash('El nombre de producto ya existe en el sistema', 'danger')
            else:
                flash('Ocurrio un error desconocido en el sistema', 'danger')

    return render_template('registrar_producto.html', titulo="Registrar Producto", form=form)

@productos.route("/productos/", methods=['GET'])
@login_required
def productos_lista():
    page = request.args.get('pagina', 1, type=int)
    response = requests.get(API_URL + "productos/" + str(page))
    return render_template('productos_lista.html', productos=response.json(), titulo="Lista de Productos")
