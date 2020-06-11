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
    api.add_resource(Compras_lista, '/compras/')
    api.add_resource(Venta_view, '/ventas/registrar')
    api.add_resource(Ventas_lista, '/ventas/')
    api.add_resource(Roles_lista, '/roles/')
    api.add_resource(Reporte_view, '/reporte/')