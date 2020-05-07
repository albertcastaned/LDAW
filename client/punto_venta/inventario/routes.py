from flask import render_template, url_for, flash, redirect, request, Blueprint
import requests, json
from punto_venta import API_URL
from punto_venta.utils import login_required

inventario = Blueprint('inventario', __name__, template_folder='templates')

@inventario.route("/inventario/", methods=['GET'])
@login_required
def inventario_lista():
    page = request.args.get('pagina', 1, type=int)
    response = requests.get(API_URL + "inventario/" + str(page))
    return render_template('inventario.html', inventario=response.json(), titulo="Inventario")
