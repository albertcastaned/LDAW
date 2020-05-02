from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask import request, Response
from flask_restful import Resource
from model import *
import os, json
from sqlalchemy.exc import IntegrityError

class Config():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = os.urandom(24)

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
api = Api(app, prefix="/api/v1")
bcrypt = Bcrypt(app)
marsh = Marshmallow(app)
Migrate(app, db,compare_type=True)

#Requests

class Productos_lista(Resource):
    def get(self, page):
        productos = Producto.query.paginate(page=page, per_page=10).items
        return productos_schema.dump(productos)

class Producto_registrar(Resource):
    def post(self):
        nuevo_producto = Producto(
            nombre_producto = request.json['nombre_producto'],
            descripcion = request.json['descripcion'],
            marca = request.json['marca'],
            precioVentaBase = request.json['precioVentaBase'],
            precioCompra = request.json['precioCompra'],
            proveedor = request.json['proveedor'],
        )
        db.session.add(nuevo_producto)
        try:
            db.session.commit()
        except IntegrityError as error:
            db.session.rollback()
            return Response(response=json.dumps(dict(error='UNIQUE constraint error')),
                    status=501, mimetype='application/json'
                )
        return usuario_schema.dump(nuevo_producto)

class Usuarios_lista(Resource):
    def get(self, page):
        usuarios = Usuario.query.paginate(page=page, per_page=10).items
        return usuarios_schema.dump(usuarios)

class Usuarios_registrar(Resource):
    def post(self):
        nuevo_usuario = Usuario(
            nombre_completo = request.json['nombre_completo'],
            nombre_usuario = request.json['nombre_usuario'],
            email = request.json['email'],
            contrasenia = bcrypt.generate_password_hash(request.json['contrasenia']),
        )

        db.session.add(nuevo_usuario)
        try:
            db.session.commit()
        except IntegrityError as error:
            db.session.rollback()
            return Response(response=json.dumps(dict(error='UNIQUE constraint error')),
                    status=501, mimetype='application/json'
                )
        return usuario_schema.dump(nuevo_usuario)

class Usuario_detalle(Resource):
    def get(self, usuario_id):
        usuario = Usuario.query.get_or_404(usuario_id)
        return usuario_schema.dump(usuario)

class Login(Resource):
    def post(self):

        username = request.json['username']
        password = request.json['password']
 
        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        user = Usuario.query.filter_by(nombre_usuario=username).first()
        
        if user and bcrypt.check_password_hash(user.contrasenia, password):
            return {
                'message': 'Successful logged in','username':str(username)
            }, 200

        return {"message":"Invalid credentials"}, 401


api.add_resource(Productos_lista, '/productos/<int:page>')
api.add_resource(Producto_registrar, '/productos/registrar/')
api.add_resource(Usuarios_lista, '/usuarios/<int:page>/')
api.add_resource(Usuarios_registrar, '/usuarios/registrar/')
api.add_resource(Usuario_detalle, '/usuario/<int:usuario_id>/')
api.add_resource(Login, '/login/')

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=6000)