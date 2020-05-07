from flask import render_template, url_for, flash, redirect, request, Blueprint, session
import requests, json
from punto_venta import API_URL
from punto_venta.utils import login_required
compras_ventas = Blueprint('compras_ventas', __name__, template_folder='templates')

@compras_ventas.route("/compras/registrar", methods=['GET', 'POST'])
@login_required
def registrar_compra():
    if request.method == 'POST':
        id_usuario = session['user_id']
        id_productos = request.form.getlist('id[]')
        precios = request.form.getlist('precioCompra[]')
        cantidades = request.form.getlist('cantidad[]')

        json_data = [{"id_usuario":id_usuario, "id_producto":producto_id, "precioCompra":precio,
        "cantidad":cantidad} for producto_id, precio, cantidad in zip(id_productos, precios, cantidades)
        ]

        response = requests.post(API_URL + "compras/registrar", json = json_data)
        if response.status_code == 201:
            flash('La compra se ha a sido registrado exitosamente', 'success')
            return redirect(url_for('inventario.inventario_lista'))
        else:
            page = request.args.get('pagina', 1, type=int)
            response = requests.get(API_URL + "inventario/" + str(page))
            flash('Ocurrio un error al registrar la compra, vuelva a intentar', 'danger')
            return render_template('registrar_compra.html', inventario=response.json(), titulo="Registrar Compra")
    else:
        page = request.args.get('pagina', 1, type=int)
        response = requests.get(API_URL + "inventario/" + str(page))
        return render_template('registrar_compra.html', inventario=response.json(), titulo="Registrar Compra")
