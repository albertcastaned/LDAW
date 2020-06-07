from database.model import *
import random

for i in range(1,100):
	nombre = "Producto" + str(i)
	marca = "Marca" + str(i)
	proveedor = "Proveedor" + str(i)
	precioC = round(random.uniform(10.00, 450.00),2)
	precioV = round(random.uniform(precioC, 500.00),2)
	producto = Producto(nombre_producto=nombre, marca=marca, proveedor=proveedor, precioCompra=precioC, precioVentaBase=precioV)
	db.session.add(producto)
	inventario = Inventario(producto=producto, cantidad=0)
	db.session.add(inventario)
	db.session.commit()
