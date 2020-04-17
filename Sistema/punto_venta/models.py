from punto_venta import db, login_manager
from flask_login import UserMixin,current_user

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Usuario(db.Model, UserMixin):
    __tablename__ = 'Usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(150))
    nombre_usuario = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False)
    contrasenia = db.Column(db.String(128), nullable=False)
    activo = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<Usuario: {}>'.format(self.nombre_usuario)

class Producto(db.Model, UserMixin):
    __tablename__ = 'Producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(150))
    descripcion = db.Column(db.String(1000))
    marca = db.Column(db.String(150))
    precioVentaBase = db.Column(db.Float)
    precioCompra = db.Column(db.Float)
    proveedor = db.Column(db.String(150))

    def __repr__(self):
        return '<Producto: {}>'.format(self.nombre_producto)
