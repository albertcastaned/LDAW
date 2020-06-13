from flask import render_template, url_for, flash, redirect, request, Blueprint, session
import requests, json
from punto_venta import API_URL
from punto_venta.utils import *
compras_ventas = Blueprint('compras_ventas', __name__, template_folder='templates')
import datetime

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
        response = requests.get(API_URL + "inventario/")
        return render_template('registrar_compra.html', inventario=response.json(), titulo="Registrar Compra")


@compras_ventas.route("/compras/", methods=['GET'])
@login_required
@is_gerente
def compras_lista():
    response = requests.get(API_URL + "compras/")
    return render_template('compras_lista.html', compras=response.json(), titulo="Lista de Compras")

@compras_ventas.route("/ventas/registrar", methods=['GET', 'POST'])
@login_required
def registrar_venta():
    if request.method == 'POST':
        id_usuario = session['user_id']
        id_productos = request.form.getlist('id[]')
        precios = request.form.getlist('precioVenta[]')
        cantidades = request.form.getlist('cantidad[]')

        json_data = [{"id_usuario":id_usuario, "id_producto":producto_id, "precioVenta":precio,
        "cantidad":cantidad} for producto_id, precio, cantidad in zip(id_productos, precios, cantidades)
        ]

        response = requests.post(API_URL + "ventas/registrar", json = json_data)
        if response.status_code == 201:
            flash('La compra ha sido registrada exitosamente', 'success')
            return redirect(url_for('inventario.inventario_lista'))
        else:
            page = request.args.get('pagina', 1, type=int)
            response = requests.get(API_URL + "inventario/" + str(page))
            flash('Ocurrio un error al registrar la venta, vuelva a intentar', 'danger')
            return render_template('registrar_venta.html', inventario=response.json(), titulo="Registrar Venta")
    else:
        response = requests.get(API_URL + "inventario/")
        return render_template('registrar_venta.html', inventario=response.json(), titulo="Registrar Venta")

@compras_ventas.route("/ventas/", methods=['GET'])
@login_required
@is_gerente
def ventas_lista():
    response = requests.get(API_URL + "ventas/")
    return render_template('ventas_lista.html', ventas=response.json(), titulo="Lista de Ventas")

@compras_ventas.route("/reporte/", methods=['GET'])
@login_required
@is_gerente
def reporte():
    if(request.args.get('año')):
        anio = request.args['año']
    else:
        anio = datetime.datetime.now().year

    response = requests.get(API_URL + "reporte/?año=" + str(anio))

    if(response.status_code != 200):
        flash('Ocurrio un error al obtener los datos. Vuelve a intentar.', 'danger')

    return render_template('reporte.html', data=response.json(), titulo="Reporte", año = anio)



@compras_ventas.route("/reportes/", methods=['GET'])
@login_required
@is_gerente
def reportes():
    start_year = datetime.datetime(2020,1,1).year
    current_year = datetime.datetime.today().year
    lista_anios = list(range(start_year, current_year+1, 1))
    return render_template('reportes_lista.html', titulo="Lista de Reportes", anios=lista_anios)