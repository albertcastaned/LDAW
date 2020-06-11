from database.model import *
import random, datetime

usuario = Usuario.query.all()[0]
numProductos = Producto.query.count()
ticketVenta = TicketVenta()
ticketCompra = TicketCompra()

start_date = datetime.date(2021, 1, 1)
end_date = datetime.date(2021, 6, 29)
for i in range(1,500):
	usuarioV = usuario
	productoV = Producto.query.filter_by(id=random.uniform(1,numProductos)).first()
	ticketV = ticketVenta
	precioV = round(random.uniform(10.00, 50.00),2)
	cantidadV = round(random.uniform(1,5),2)
	totalV = round(precioV * cantidadV,2)
	time_between_dates = end_date - start_date
	days_between_dates = time_between_dates.days
	random_number_of_days = random.randrange(days_between_dates)
	random_date = start_date + datetime.timedelta(days=random_number_of_days)
	venta = Venta(usuario=usuarioV, producto=productoV, 
		ticket=ticketV, precioVenta=precioV, cantidad=cantidadV, 
		total=totalV, fecha=random_date)
	db.session.add(venta)
	usuarioC = usuario
	productoC = Producto.query.filter_by(id=random.uniform(1,numProductos)).first()
	ticketC = ticketCompra
	precioC = round(random.uniform(precioV - 20, precioV + 10),2)
	cantidadC = cantidadV
	totalC = round(precioC * cantidadC, 2)
	time_between_dates = end_date - start_date
	days_between_dates = time_between_dates.days
	random_number_of_days = random.randrange(days_between_dates)
	random_date = start_date + datetime.timedelta(days=random_number_of_days)
	compra = Compra(usuario=usuarioC, producto=productoC, 
		ticket=ticketC, precioCompra=precioC, cantidad=cantidadC, 
		total=totalC, fecha=random_date)
	db.session.add(compra)

db.session.commit()


print("\n\nSe crearon las ventas y compras de muestra exitosamente :)\n\n")
