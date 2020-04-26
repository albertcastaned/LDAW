from flask import render_template, url_for, flash, redirect, request, Blueprint
from punto_venta.productos.forms import *
from punto_venta.models import Producto
from punto_venta import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

productos = Blueprint('productos', __name__, template_folder='templates')

@productos.route("/productos/registrar", methods=['GET', 'POST'])
def registrar_producto():
    form = RegistarProductoForm()
    if form.validate_on_submit():
        producto = Producto(
            nombre_producto=form.nombre_producto.data,
            descripcion=form.descripcion_producto.data,
            marca=form.marca_producto.data,
            precioVentaBase=form.precio_venta.data,
            precioCompra=form.precio_compra.data,
            proveedor=form.proveedor.data)
        db.session.add(producto)
        db.session.commit()
        print("Nuevo Producto Creado")
        flash('El producto a sido registrado exitosamente', 'success')
        return redirect(url_for('productos.productos_lista'))
    return render_template('registrar_producto.html', titulo="Registrar Producto", form=form)

@productos.route("/productos/", methods=['GET'])
def productos_lista():
    page = request.args.get('pagina', 1, type=int)
    productos = Producto.query.paginate(page=page, per_page=20)
    return render_template('productos_lista.html', productos=productos, titulo="Lista de Productos")
