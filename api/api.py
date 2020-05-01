from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_login import UserMixin,current_user
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import os

class Config():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = os.urandom(24)

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
api = Api(app)
bcrypt = Bcrypt(app)
marsh = Marshmallow(app)
Migrate(app, db,compare_type=True)
login_manager = LoginManager(app)
login_manager.login_view = 'usuarios.login'
login_manager.login_message_category = 'info'

#Modelo
Base = declarative_base()

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Usuario(db.Model, UserMixin, Base):
    __tablename__ = 'Usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(150))
    nombre_usuario = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False)
    contrasenia = db.Column(db.String(128), nullable=False)
    activo = db.Column(db.Boolean, default=True)

    compra_productos = db.relationship('Producto', secondary='Compras')
    venta_productos = db.relationship('Producto', secondary='Ventas')

    def __repr__(self):
        return '<Usuario: {}>'.format(self.nombre_usuario)

class UsuarioSchema(marsh.Schema):
    class Meta:
        fields = ("id", "nombre_completo", "nombre_usuario", "email", "activo")
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

class Producto(db.Model, UserMixin, Base):
    __tablename__ = 'Producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.String(1000))
    marca = db.Column(db.String(150),nullable=False)
    precioVentaBase = db.Column(db.Float,nullable=False)
    precioCompra = db.Column(db.Float,nullable=False)
    proveedor = db.Column(db.String(150),nullable=False)

    compra_usuarios = db.relationship('Usuario', secondary='Compras')
    venta_usuarios = db.relationship('Usuario', secondary='Ventas')


    def __repr__(self):
        return '<Producto: {}>'.format(self.nombre_producto)


class Compra(db.Model, Base):
    __tablename__ = 'Compras'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuarios.id'))
    id_producto = db.Column(db.Integer, db.ForeignKey('Producto.id'))
    precioCompra = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Compra: {}>'.format(self.id)


class Venta(db.Model, Base):
    __tablename__ = 'Ventas'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuarios.id'))
    id_producto = db.Column(db.Integer, db.ForeignKey('Producto.id'))
    precioVenta = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Venta: {}>'.format(self.id)


class Inventario(db.Model, Base):
    __tablename__ = 'Inventario'
    id = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('Producto.id'))
    cantidad = db.Column(db.Float, nullable=False)
    producto = relationship(Producto, backref=backref('inventarios', uselist=True))

    def __repr__(self):
        return '<Inventario: {}>'.format(self.id)


#Requests
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
            contrasenia = request.json['contrasenia'],
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return usuario_schema.dump(nuevo_usuario)

class Usuario_detalle(Resource):
    def get(self, usuario_id):
        usuario = Usuario.query.get_or_404(usuario_id)
        return usuario_schema.dump(usuario)

api.add_resource(Usuarios_lista, '/api/v1/usuarios')
api.add_resource(Usuarios_registrar, '/api/v1/usuarios/registrar')
api.add_resource(Usuario_detalle, '/api/v1/usuarios/<int:usuario_id>')


if __name__ == '__main__':
    app.run(debug=True)