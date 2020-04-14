from .. import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    contrasenia = db.Column(db.String(128))

    def __repr__(self):
        return '<Usuario {}>'.format(self.nombre_usuario)