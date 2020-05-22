from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from .db import db, marsh
from flask_bcrypt import generate_password_hash, check_password_hash
from marshmallow import fields
#Modelo
Base = declarative_base()

class Usuario(db.Model , Base):
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

class Producto(db.Model, Base):
    __tablename__ = 'Producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(150), nullable=False, unique=True)
    descripcion = db.Column(db.String(1000))
    marca = db.Column(db.String(150),nullable=False)
    precioVentaBase = db.Column(db.Float,nullable=False)
    precioCompra = db.Column(db.Float,nullable=False)
    proveedor = db.Column(db.String(150),nullable=False)

    compra_usuarios = db.relationship('Usuario', secondary='Compras')
    venta_usuarios = db.relationship('Usuario', secondary='Ventas')


    def __repr__(self):
        return '<Producto: {}>'.format(self.nombre_producto)

class ProductoSchema(marsh.Schema):
    class Meta:
        fields = ("id", "nombre_producto", "descripcion", "marca", "precioVentaBase", "precioCompra","proveedor")

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)


class Compra(db.Model, Base):
    __tablename__ = 'Compras'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuarios.id'))
    id_producto = db.Column(db.Integer, db.ForeignKey('Producto.id'))
    precioCompra = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    producto = relationship(Producto, backref=backref('compras', uselist=True))
    usuario = relationship(Usuario, backref=backref('compras', uselist=True))

    def __repr__(self):
        return '<Compra: {}>'.format(self.id)

class CompraSchema(marsh.Schema):
    precioCompra = fields.Float()
    cantidad = fields.Float()
    total = fields.Float()
    fecha = fields.DateTime()
    producto = fields.Nested(ProductoSchema)
    usuario = fields.Nested(UsuarioSchema)

compra_schema = CompraSchema()
compras_schema = CompraSchema(many=True)


class Venta(db.Model, Base):
    __tablename__ = 'Ventas'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuarios.id'))
    id_producto = db.Column(db.Integer, db.ForeignKey('Producto.id'))
    precioVenta = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    producto = relationship(Producto, backref=backref('ventas', uselist=True))
    usuario = relationship(Usuario, backref=backref('ventas', uselist=True))

    def __repr__(self):
        return '<Venta: {}>'.format(self.id)

class VentaSchema(marsh.Schema):
    precioVenta = fields.Float()
    cantidad = fields.Float()
    total = fields.Float()
    fecha = fields.DateTime()
    producto = fields.Nested(ProductoSchema)
    usuario = fields.Nested(UsuarioSchema)

venta_schema = VentaSchema()
ventas_schema = VentaSchema(many=True)


class Inventario(db.Model, Base):
    __tablename__ = 'Inventario'
    id = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('Producto.id'))
    cantidad = db.Column(db.Float, nullable=False)
    producto = relationship(Producto, backref=backref('inventarios', uselist=True))

    def __repr__(self):
        return '<Inventario: {}>'.format(self.id)

class InventarioSchema(marsh.Schema):
    cantidad = fields.Integer()
    producto = fields.Nested(ProductoSchema)

inventario_schema = InventarioSchema(many=True)
