from punto_venta import db, login_manager
from flask_login import UserMixin,current_user
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

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
