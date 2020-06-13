from flask import render_template, Blueprint, jsonify, request, session
from mailjet_rest import Client
import os
from punto_venta.utils import *

api_key = 'ba517abc3e1f70ef85473df2f055dd32'
api_secret = 'a7c4d83a2f962fc2ab9b39993e104e60'

correos = [
    {
        'Email':'albertcastaned@gmail.com'
    },
    {
        'Email':'A01250647@itesm.mx'
    }
]

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
@login_required
def index():
    esGerente = False
    if 'roles' in session:
        for rol in session['roles']:
            if rol['nombre'].lower() == "Gerente".lower():
                esGerente = True
    return render_template('home.html',titulo='Home', esGerente=esGerente)

@main.route("/correo", methods=['POST'])
def send_mail():    
    html = '<table><thead>'
    for header in request.json['header']:
        html = html + '<th>' + header + '</th>'
    
    html = html + '</thead><tbody>'

    for data in request.json['body']:
        html = html + '<tr>'
        for element in data:
            html = html + '<td>' + element + '</td>'
        html = html + '</tr>'
    
    html = html + '</tbody></table>'

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
    'Messages': [
        {
        "From": {
            "Email": "albertcastaned@gmail.com",
            "Name": "Agroservicios La Guadalupana"
        },
        "To": correos,
        "Subject": "Reporte",
        "TextPart": "Reporte generado por punto de venta",
        "HTMLPart": html,
        "CustomID": "ReporteGeneradoPuntoVenta"
        }
    ]
    }
    result = mailjet.send.create(data=data)
    if(result.status_code != 200):
        abort(500)
    return jsonify(status="success")
