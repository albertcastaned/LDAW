from database.model import *
from database.db import bcrypt

rol1 = Rol(id=1, nombre='Gerente')
rol2 = Rol(id=2, nombre='Asistente')

db.session.add(rol1)
db.session.add(rol2)

superUsuario = Usuario(nombre_completo="Super Usuario",
    nombre_usuario="admin", contrasenia=bcrypt.generate_password_hash("super1234"), email="admin@gmail.com")

superUsuario.roles.append(rol1)
superUsuario.roles.append(rol2)

db.session.add(superUsuario)

db.session.commit()

print("\n\nSe crearon los roles y el super usuario exitosamente :)\n\n")