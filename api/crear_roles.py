from database.model import *

rol1 = Rol(id=1, nombre='Administrador')
rol2 = Rol(id=2, nombre='Gerente')
rol3 = Rol(id=3, nombre='Asistente')

db.session.add(rol1)
db.session.add(rol2)
db.session.add(rol3)

db.session.commit()