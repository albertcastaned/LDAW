import sys, os


from punto_venta.usuarios.models import Usuario
from conftest import app, client
def test_new_usuario():
    usuario = Usuario(nombre_completo='Alberto Castaneda', nombre_usuario='albertcastaned', 
    email='a@gmail.com', contrasenia='password123', activo=True)
    assert usuario.nombre_completo == "Alberto Castaneda"
    assert usuario.nombre_usuario == "albertcastaned"
    assert usuario.email == "a@gmail.com"
    assert usuario.contrasenia == "password123"
    assert usuario.activo == True

def test_get_view(client):
    resp = client.get("/usuarios/registrar")
    assert resp.status_code == 200