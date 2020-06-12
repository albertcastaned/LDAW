from flask import render_template, url_for, flash, redirect, request, Blueprint
from punto_venta.productos.forms import *
import requests, json
from punto_venta import API_URL
from punto_venta.utils import *

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

@productos.route("/productos/modificar/", methods=['GET', 'PUT', 'POST'])
@login_required
def modificar_producto():
    form = RegistarProductoForm()
    if form.validate_on_submit():
        producto = requests.get(API_URL + "productos/modificar/")
        post_data = {
            'nombre_producto':form.nombre_producto.data,
            'descripcion':form.descripcion_producto.data,
            'marca':form.marca_producto.data,
            'precioVentaBase':str(form.precio_venta.data),
            'precioCompra':str(form.precio_compra.data),
            'proveedor':form.proveedor.data
        }
        form.nombre_producto.data : producto.nombre_producto
        form.descripcion_producto.data : producto.descripcion_producto
        form.marca_producto.data : producto.marca_producto
        form.precio_venta.data : producto.precio_venta
        form.precio_compra.data : producto.precio_compra
        form.proveedor.data : producto.proveedor

        response = requests.post(API_URL + "productos/modificar/", json = post_data)

        if(response.status_code == 200 or response.status_code == 201):
            flash('El producto a sido modificado exitosamente', 'success')
            return redirect(url_for('productos.productos_lista'))
        else:
            if(response.status_code == 501):
                flash('El nombre de producto ya existe en el sistema', 'danger')
            else:
                flash('Ocurrio un error desconocido en el sistema', 'danger')

    return render_template('modificar_producto.html', titulo="Modificar Producto", form=form)

@productos.route("/productos/", methods=['GET'])
@login_required
@is_administrator
def productos_lista():
    response = requests.get(API_URL + "productos/")
    return render_template('productos_lista.html', productos=response.json(), titulo="Lista de Productos")
