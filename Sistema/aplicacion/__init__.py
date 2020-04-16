from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from applicacion.config import Config


db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)

    migrate = Migrate(app, db)

    from aplicacion.routes import main
    from aplicacion.compras_ventas.routes import compras_ventas
    from punaplicacionto_venta.usuarios.routes import usuarios
    from aplicacion.productos.routes import productos
    app.register_blueprint(usuarios)
    app.register_blueprint(productos)
    app.register_blueprint(main)
    app.register_blueprint(compras_ventas)

    return app