from flask import render_template, url_for, flash, redirect, request, Blueprint
import requests, json
from punto_venta import API_URL
from punto_venta.utils import login_required

inventario = Blueprint('inventario', __name__, template_folder='templates')

@inventario.route("/inventario/", methods=['GET'])
@login_required
def inventario_lista():
    response = requests.get(API_URL + "inventario/")
    return render_template('inventario.html', inventario=response.json(), titulo="Inventario")
