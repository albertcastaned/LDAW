import sys, os
from punto_venta.usuarios.forms import *
from conftest import app, client


def test_get_view(client):
    with client.session_transaction() as session:
        session['logged_in'] = True
    resp = client.get("/usuarios/registrar")
    assert resp.status_code == 200

def test_registrarUusario_vacios(client):
    input_nombre_usuario = ""
    input_contrasenia = ""
    input_confirmar_contrasenia = input_contrasenia
    input_email=""
    input_nombre_completo=""

    data = {
    'nombre_usuario': input_nombre_usuario,
    'contrasenia': input_contrasenia,
    'confirmar_contrasenia': input_confirmar_contrasenia,
    'email': input_email,
    'nombre_completo': input_nombre_completo,
    }

    form = RegistarUsuarioForm(data=data)
    
    assert False == form.validate()

def test_registrarUusario_contrasenia_incorrecta(client):
    input_nombre_usuario = "albertcastaned"
    input_contrasenia = "pass1234"
    input_confirmar_contrasenia = "pass"
    input_email="albert@gmail.com"
    input_nombre_completo="Alberto Castaneda"

    data={
    'nombre_usuario': input_nombre_usuario,
    'contrasenia': input_contrasenia,
    'confirmar_contrasenia': input_confirmar_contrasenia,
    'email': input_email,
    'nombre_completo': input_nombre_completo,

    }
    
    form = RegistarUsuarioForm(data=data)
    
    assert False == form.validate()


def test_registrarUusario_valido(client):
    input_nombre_usuario = "albertcastaned343"
    input_contrasenia = "pass1234"
    input_confirmar_contrasenia = input_contrasenia
    input_email="albert@gmail.com"
    input_nombre_completo="Alberto Castaneda"

    data={
    'nombre_usuario': input_nombre_usuario,
    'contrasenia': input_contrasenia,
    'confirmar_contrasenia': input_confirmar_contrasenia,
    'email': input_email,
    'nombre_completo': input_nombre_completo,

    }
    
    form = RegistarUsuarioForm(data=data)
    print(form.validate())
    assert True == form.validate()