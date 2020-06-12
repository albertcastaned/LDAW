from flask import render_template, Blueprint, jsonify, request
from mailjet_rest import Client
import os
api_key = 'ba517abc3e1f70ef85473df2f055dd32'
api_secret = 'a7c4d83a2f962fc2ab9b39993e104e60'

#TODO: Cambiar a correos que utilizaran
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
def index():
    return render_template('home.html',titulo='Home')


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
    print(result.status_code)
    return jsonify(status="success")
