import sys, os


from punto_venta.models import *
from punto_venta.usuarios.forms import *
from conftest import app, client
def test_new_usuario(session):
    usuario = Usuario(nombre_completo='Alberto Castaneda', nombre_usuario='albertcastaned', 
    email='a@gmail.com', contrasenia='password123', activo=True)
    assert usuario.nombre_completo == "Alberto Castaneda"
    assert usuario.nombre_usuario == "albertcastaned"
    assert usuario.email == "a@gmail.com"
    assert usuario.contrasenia == "password123"
    assert usuario.activo == True

    session.add(usuario)
    session.commit()
    assert usuario.id > 0

def test_get_view(client):
    resp = client.get("/usuarios/registrar")
    assert resp.status_code == 200

def test_registro_vacios(client, session):
    input_nombre_usuario = ""
    input_contrasenia = ""
    input_confirmar_contrasenia = input_contrasenia
    input_email=""
    input_nombre_completo=""

    response = client.post("/usuarios/registrar", 
        data={
        'nombre_usuario': input_nombre_usuario,
        'contrasenia': input_contrasenia,
        'confirmar_contrasenia': input_confirmar_contrasenia,
        'email': input_email,
        'nombre_completo': input_nombre_completo,

        }, follow_redirects=True
    )
    usuario = Usuario.query.filter(Usuario.nombre_usuario == input_nombre_usuario).first()
    assert usuario == None

def test_registro_contrasenia_incorrecta(client, session):
    input_nombre_usuario = "albertcastaned"
    input_contrasenia = "pass1234"
    input_confirmar_contrasenia = "pass"
    input_email="albert@gmail.com"
    input_nombre_completo="Alberto Castaneda"

    response = client.post("/usuarios/registrar", 
        data={
        'nombre_usuario': input_nombre_usuario,
        'contrasenia': input_contrasenia,
        'confirmar_contrasenia': input_confirmar_contrasenia,
        'email': input_email,
        'nombre_completo': input_nombre_completo,

        }, follow_redirects=True
    )
    usuario = Usuario.query.filter(Usuario.nombre_usuario == input_nombre_usuario).first()
    assert usuario == None

def test_registro_usuario_existente(client, session):
    usuario = Usuario(nombre_completo='Alberto Castaneda', nombre_usuario='albertcastaned', 
    email='a@gmail.com', contrasenia='password123', activo=True)
    session.add(usuario)
    session.commit()

    input_nombre_usuario = "albertcastaned"
    input_contrasenia = "pass1234"
    input_confirmar_contrasenia = input_contrasenia
    input_email="albert@gmail.com"
    input_nombre_completo="Alberto Castaneda"

    response = client.post("/usuarios/registrar", 
        data={
        'nombre_usuario': input_nombre_usuario,
        'contrasenia': input_contrasenia,
        'confirmar_contrasenia': input_confirmar_contrasenia,
        'email': input_email,
        'nombre_completo': input_nombre_completo,

        }, follow_redirects=True
    )
    assert b"El nombre de ese usuario ya esta regisrado en el sistema" in response.data

def test_registro_valido(client, session):
    input_nombre_usuario = "albertcastaned343"
    input_contrasenia = "pass1234"
    input_confirmar_contrasenia = input_contrasenia
    input_email="albert@gmail.com"
    input_nombre_completo="Alberto Castaneda"

    response = client.post("/usuarios/registrar", 
        data={
        'nombre_usuario': input_nombre_usuario,
        'contrasenia': input_contrasenia,
        'confirmar_contrasenia': input_confirmar_contrasenia,
        'email': input_email,
        'nombre_completo': input_nombre_completo,

        }, follow_redirects=True
    )
    usuario = Usuario.query.filter(Usuario.nombre_usuario == input_nombre_usuario).first()
    assert usuario
    assert usuario.nombre_usuario == input_nombre_usuario
    assert usuario.contrasenia != input_contrasenia
    assert usuario.email == input_email
    assert usuario.nombre_completo == input_nombre_completo