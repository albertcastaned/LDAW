
from flask import Flask, request, Response, jsonify
from database.model import *
from database.db import bcrypt
from flask_restful import Resource
import os, json
from datetime import date
from sqlalchemy.exc import IntegrityError

#Requests
class Productos_lista(Resource):
    def get(self):
        productos = Producto.query.all()
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
        return 'OK', 201

class Usuarios_lista(Resource):
    def get(self):
        usuarios = Usuario.query.all()
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
        except IntegrityError:
            db.session.rollback()
            return Response(response=json.dumps(dict(error='UNIQUE constraint error')),
                    status=501, mimetype='application/json'
                )
        return 'OK', 201

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
    def get(self):
        inventario = Inventario.query.all()
        return inventario_schema.dump(inventario)

class Compra_view(Resource):
    def post(self):
        compras = request.json
        print(compras)
        for compra in compras:
            nueva_compra = Compra(
                id_usuario = compra['id_usuario'],
                id_producto = compra['id_producto'],
                precioCompra = compra['precioCompra'],
                cantidad = compra['cantidad'],
                total = float(compra['precioCompra']) * float(compra['cantidad']),
                fecha = date.today()
            )
            db.session.add(nueva_compra)

            registro_inventario = Inventario.query.filter_by(id_producto=nueva_compra.id_producto).first()
            registro_inventario.cantidad = float(registro_inventario.cantidad) + float(nueva_compra.cantidad)
            print(nueva_compra)
        db.session.commit()

        return 'OK', 201

class Compras_lista(Resource):
    def get(self):
        compras = Compra.query.all()
        return compras_schema.dump(compras)

class Venta_view(Resource):
    def post(self):
        print("Hola")
        ventas = request.json
        print("Hola3")
        print(ventas)
        for venta in ventas:
            nueva_venta = Venta(
                id_usuario = venta['id_usuario'],
                id_producto = venta['id_producto'],
                precioVenta = venta['precioVenta'],
                cantidad = venta['cantidad'],
                total = float(venta['precioVenta']) * float(venta['cantidad']),
                fecha = date.today()
            )
            print("Hola2")
            db.session.add(nueva_venta)

            registro_inventario = Inventario.query.filter_by(id_producto=nueva_venta.id_producto).first()
            registro_inventario.cantidad = float(registro_inventario.cantidad) - float(nueva_venta.cantidad)
            print(registro_inventario)
            print(nueva_venta)
        db.session.commit()

        return 'OK', 201

class Ventas_lista(Resource):
    def get(self):
        ventas = Venta.query.all()
        return ventas_schema.dump(ventas)
