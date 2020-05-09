from .requests import *

def initialize_routes(api):
    api.add_resource(Productos_lista, '/productos/')
    api.add_resource(Producto_registrar, '/productos/registrar')
    api.add_resource(Usuarios_lista, '/usuarios/')
    api.add_resource(Usuarios_registrar, '/usuarios/registrar')
    api.add_resource(Usuario_detalle, '/usuario/<int:usuario_id>')
    api.add_resource(Login, '/login')
    api.add_resource(Inventario_view, '/inventario/')
    api.add_resource(Compra_view, '/compras/registrar')