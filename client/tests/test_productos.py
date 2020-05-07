import sys, os

from punto_venta.productos.forms import *
from conftest import app, client


def test_get_view(client):
    with client.session_transaction() as session:
        session['logged_in'] = True
    resp = client.get("/productos/registrar")
    resp.status_code == 200

def test_registrarProducto_vacios(client):
    data_nombre_producto = ""
    data_descripcion = ""
    data_marca = ""
    data_precioVentaBase = 2
    data_precioCompra = 2
    data_proveedor = ""

    data={
    'nombre_producto': data_nombre_producto,
    'descripcion_producto': data_descripcion,
    'marca_producto': data_marca,
    'precio_venta': data_precioVentaBase,
    'precio_compra': data_precioCompra,
    'proveedor': data_proveedor,
    }

    form = RegistarProductoForm(data=data)

    assert False == form.validate()

def test_registrarProducto_campos_ilegales(client):
    data_nombre_producto = "@"
    data_descripcion = "/"
    data_marca = "><"
    data_precioVentaBase = 15
    data_precioCompra = 15
    data_proveedor = '<script>alert("hello")</script>'

    data={
    'nombre_producto': data_nombre_producto,
    'descripcion_producto': data_descripcion,
    'marca_producto': data_marca,
    'precio_venta': data_precioVentaBase,
    'precio_compra': data_precioCompra,
    'proveedor': data_proveedor,
    }

    form = RegistarProductoForm(data=data)

    assert False == form.validate()


def test_registrarProducto_valores_cero(client):
    data_nombre_producto = "prueba"
    data_descripcion = "prueba"
    data_marca = "prueba"
    data_precioVentaBase = 0
    data_precioCompra = 0
    data_proveedor = "prueba"

    data={
    'nombre_producto': data_nombre_producto,
    'descripcion_producto': data_descripcion,
    'marca_producto': data_marca,
    'precio_venta': data_precioVentaBase,
    'precio_compra': data_precioCompra,
    'proveedor': data_proveedor,
    }

    form = RegistarProductoForm(data=data)

    assert False == form.validate()

def test_registrarProducto_valores_negativo(client):
    data_nombre_producto = "prueba"
    data_descripcion = "prueba"
    data_marca = "prueba"
    data_precioVentaBase = -5
    data_precioCompra = -2
    data_proveedor = "prueba"
    data={
    'nombre_producto': data_nombre_producto,
    'descripcion_producto': data_descripcion,
    'marca_producto': data_marca,
    'precio_venta': data_precioVentaBase,
    'precio_compra': data_precioCompra,
    'proveedor': data_proveedor,
    }

    form = RegistarProductoForm(data=data)

    assert False == form.validate()


def test_registrarProducto_exitoso(client):
    data_nombre_producto = "prueba"
    data_descripcion = "prueba"
    data_marca = "prueba"
    data_precioVentaBase = 50.250
    data_precioCompra = 20.2
    data_proveedor = "prueba"
    data={
    'nombre_producto': data_nombre_producto,
    'descripcion_producto': data_descripcion,
    'marca_producto': data_marca,
    'precio_venta': data_precioVentaBase,
    'precio_compra': data_precioCompra,
    'proveedor': data_proveedor,
    }

    form = RegistarProductoForm(data=data)

    assert True == form.validate()