from database.model import *

Venta.query.delete()
Compra.query.delete()

db.session.commit()
