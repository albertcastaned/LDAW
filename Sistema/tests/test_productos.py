import sys, os

from punto_venta import bcrypt

from punto_venta.models import *
from punto_venta.productos.forms import *
from conftest import app, client

def test_new_producto(session):
    producto = Producto(nombre_producto='Fuchicol', 
        descripcion="", marca="marca",precioVentaBase=2.50,
        precioCompra=12.65, proveedor="Proveedor")

    session.add(producto)
    session.commit()
    producto.id > 0

def test_get_view(client):
    resp = client.get("/productos/registrar")
    resp.status_code == 200

def test_registrarUusario_vacios(client, session):
    data_nombre_producto = ""
    data_descripcion = ""
    data_marca = ""
    data_precioVentaBase = 2
    data_precioCompra = 2
    data_proveedor = ""

    response = client.post("/productos/registrar", 
        data={
        'nombre_producto': data_nombre_producto,
        'descripcion_producto': data_descripcion,
        'marca_producto': data_marca,
        'precio_venta': data_precioVentaBase,
        'precio_compra': data_precioCompra,
        'proveedor': data_proveedor,


        }, follow_redirects=True
    )
    producto = Producto.query.filter(Producto.nombre_producto == data_nombre_producto).first()
    assert producto == None

def test_registrarUusario_valores_cero(client, session):
    data_nombre_producto = "prueba"
    data_descripcion = "prueba"
    data_marca = "prueba"
    data_precioVentaBase = 0
    data_precioCompra = 0
    data_proveedor = "prueba"

    response = client.post("/productos/registrar", 
        data={
        'nombre_producto': data_nombre_producto,
        'descripcion_producto': data_descripcion,
        'marca_producto': data_marca,
        'precio_venta': data_precioVentaBase,
        'precio_compra': data_precioCompra,
        'proveedor': data_proveedor,

        }, follow_redirects=True
    )
    producto = Producto.query.filter(Producto.nombre_producto == data_nombre_producto).first()
    assert producto == None

def test_registrarUusario_valores_negativo(client, session):
    data_nombre_producto = "prueba"
    data_descripcion = "prueba"
    data_marca = "prueba"
    data_precioVentaBase = -5
    data_precioCompra = -2
    data_proveedor = "prueba"

    response = client.post("/productos/registrar", 
        data={
        'nombre_producto': data_nombre_producto,
        'descripcion_producto': data_descripcion,
        'marca_producto': data_marca,
        'precio_venta': data_precioVentaBase,
        'precio_compra': data_precioCompra,
        'proveedor': data_proveedor,


        }, follow_redirects=True
    )
    producto = Producto.query.filter(Producto.nombre_producto == data_nombre_producto).first()
    assert producto == None

def test_registrarUusario_minimo(client, session):
    data_nombre_producto = "p"
    data_descripcion = "p"
    data_marca = "p"
    data_precioVentaBase = 50.250
    data_precioCompra = 20.2
    data_proveedor = "p"

    response = client.post("/productos/registrar", 
        data={
        'nombre_producto': data_nombre_producto,
        'descripcion_producto': data_descripcion,
        'marca_producto': data_marca,
        'precio_venta': data_precioVentaBase,
        'precio_compra': data_precioCompra,
        'proveedor': data_proveedor,

        }, follow_redirects=True
    )
    producto = Producto.query.filter(Producto.nombre_producto == data_nombre_producto).first()
    assert producto

def test_registrarUusario_exitoso(client, session):
    data_nombre_producto = "prueba"
    data_descripcion = "prueba"
    data_marca = "prueba"
    data_precioVentaBase = 50.250
    data_precioCompra = 20.2
    data_proveedor = "prueba"

    response = client.post("/productos/registrar", 
        data={
        'nombre_producto': data_nombre_producto,
        'descripcion_producto': data_descripcion,
        'marca_producto': data_marca,
        'precio_venta': data_precioVentaBase,
        'precio_compra': data_precioCompra,
        'proveedor': data_proveedor,

        }, follow_redirects=True
    )
    producto = Producto.query.filter(Producto.nombre_producto == data_nombre_producto).first()
    assert producto
