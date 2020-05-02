from flask import Flask
from flask_migrate import Migrate
from punto_venta.config import Config

API_URL = 'http://127.0.0.1:6000/api/v1/'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    from punto_venta.routes import main
    from punto_venta.compras_ventas.routes import compras_ventas
    from punto_venta.usuarios.routes import usuarios
    from punto_venta.productos.routes import productos
    app.register_blueprint(usuarios)
    app.register_blueprint(productos)
    app.register_blueprint(main)
    app.register_blueprint(compras_ventas)

    return app