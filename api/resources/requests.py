
from flask import Flask, request, Response, jsonify
from database.model import *
from database.db import bcrypt
from flask_restful import Resource
import os, json
from datetime import date
#Requests
class Productos_lista(Resource):
    def get(self, page):
        productos = Producto.query.paginate(page=page, per_page=10).items
        return producto_schema.dump(productos)

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

        nuevo_inventario = Inventario(
            producto = nuevo_producto,
            cantidad = 0,
        )

        db.session.add(nuevo_inventario)

        try:
            db.session.commit()
        except IntegrityError as error:
            db.session.rollback()
            return Response(response=json.dumps(dict(error='UNIQUE constraint error')),
                    status=501, mimetype='application/json'
                )
        return producto_schema.dump(nuevo_producto)

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
                'message': 'Successful logged in','username':str(username), 'id':int(user.id)
            }, 200

        return {"message":"Invalid credentials"}, 401

class Inventario_view(Resource):
    def get(self, page):
        inventario = Inventario.query.paginate(page=page, per_page=10).items
        return inventario_schema.dump(inventario)
    
class Compra_view(Resource):
    def post(self):

        nueva_compra = Compra(
            id_usuario = request.json['id_usuario'],
            id_producto = request.json['id_producto'],
            precioCompra = request.json['precioCompra'],
            cantidad = request.json['cantidad'],
            total = float(request.json['precioCompra']) * float(request.json['cantidad']),
            fecha = date.today()
        )
        db.session.add(nueva_compra)

        registro_inventario = Inventario.query.filter_by(id_producto=nueva_compra.id_producto).first()
        registro_inventario.cantidad = registro_inventario.cantidad + nueva_compra.cantidad
        
        db.session.commit()

        return compras_schema.dump(nueva_compra)