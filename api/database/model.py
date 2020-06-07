from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from .db import db, marsh
from flask_bcrypt import generate_password_hash, check_password_hash
from marshmallow import fields
#Modelo
Base = declarative_base()

roles_usuarios = db.Table(
    'roles_usuarios',
    db.Column('usuario_id', db.Integer(), db.ForeignKey('Usuarios.id')),
    db.Column('rol_id', db.Integer(), db.ForeignKey('Roles.id'))
)

class Usuario(db.Model , Base):
    __tablename__ = 'Usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(150))
    nombre_usuario = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False)
    contrasenia = db.Column(db.String(128), nullable=False)
    activo = db.Column(db.Boolean, default=True)

    # Agregar con usuario.roles.append(rol)
    roles = db.relationship('Rol', secondary=roles_usuarios)

    compra_productos = db.relationship('Producto', secondary='Compras')
    venta_productos = db.relationship('Producto', secondary='Ventas')

    def __repr__(self):
        return '<Usuario: {}, Roles: {}>'.format(self.nombre_usuario, self.roles)

class Rol(db.Model):
    __tablename__ = 'Roles'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return '<Rol: {}>'.format(self.nombre)

class RolSchema(marsh.Schema):
    class Meta:
        fields = ("id", "nombre")

rol_schema = RolSchema()
roles_schema = RolSchema(many=True)

class UsuarioSchema(marsh.Schema):
    id = fields.Integer()
    nombre_completo = fields.String()
    nombre_usuario = fields.String()
    email = fields.String()
    activo = fields.Boolean()
    roles = fields.Nested(roles_schema)

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


class TicketCompra(db.Model):
    __tablename__ = 'TicketCompras'
    id = db.Column(db.Integer, primary_key=True)

class Compra(db.Model, Base):
    __tablename__ = 'Compras'
    id = db.Column(db.Integer, primary_key=True)
    id_ticket = db.Column(db.Integer, db.ForeignKey('TicketCompras.id'))
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuarios.id'))
    id_producto = db.Column(db.Integer, db.ForeignKey('Producto.id'))
    precioCompra = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    ticket = relationship(TicketCompra, backref=backref('compras', uselist=True))
    producto = relationship(Producto, backref=backref('compras', uselist=True))
    usuario = relationship(Usuario, backref=backref('compras', uselist=True))

    def __repr__(self):
        return '<Compra: {}, Ticket: {}>'.format(self.id, self.id_ticket)

class CompraSchema(marsh.Schema):
    precioCompra = fields.Float()
    cantidad = fields.Float()
    total = fields.Float()
    fecha = fields.DateTime()
    id_ticket = fields.Integer()
    producto = fields.Nested(ProductoSchema)
    usuario = fields.Nested(UsuarioSchema)

compra_schema = CompraSchema()
compras_schema = CompraSchema(many=True)

class TicketVenta(db.Model):
    __tablename__ = 'TicketVentas'
    id = db.Column(db.Integer, primary_key=True)

class Venta(db.Model, Base):
    __tablename__ = 'Ventas'
    id = db.Column(db.Integer, primary_key=True)
    id_ticket = db.Column(db.Integer, db.ForeignKey('TicketVentas.id'))
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuarios.id'))
    id_producto = db.Column(db.Integer, db.ForeignKey('Producto.id'))
    precioVenta = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    ticket = relationship(TicketVenta, backref=backref('ventas', uselist=True))
    producto = relationship(Producto, backref=backref('ventas', uselist=True))
    usuario = relationship(Usuario, backref=backref('ventas', uselist=True))

    def __repr__(self):
        return '<Venta: {}, Ticket: {}>'.format(self.id, self.id_ticket)

class VentaSchema(marsh.Schema):
    precioVenta = fields.Float()
    cantidad = fields.Float()
    total = fields.Float()
    fecha = fields.DateTime()
    id_ticket = fields.Integer()
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
