
CREATE TABLE "Usuarios" (
	id INTEGER NOT NULL, 
	nombre_completo VARCHAR(150), 
	nombre_usuario VARCHAR(20) NOT NULL, 
	email VARCHAR(120) NOT NULL, 
	contrasenia VARCHAR(128) NOT NULL, 
	activo BOOLEAN, 
	PRIMARY KEY (id), 
	UNIQUE (nombre_usuario)
)



CREATE TABLE "Producto" (
	id INTEGER NOT NULL, 
	nombre_producto VARCHAR(150) NOT NULL, 
	descripcion VARCHAR(1000), 
	marca VARCHAR(150) NOT NULL, 
	"precioVentaBase" FLOAT NOT NULL, 
	"precioCompra" FLOAT NOT NULL, 
	proveedor VARCHAR(150) NOT NULL, 
	PRIMARY KEY (id)
)



CREATE TABLE "Compras" (
	id INTEGER NOT NULL, 
	id_usuario INTEGER, 
	id_producto INTEGER, 
	"precioCompra" FLOAT NOT NULL, 
	cantidad FLOAT NOT NULL, 
	total FLOAT NOT NULL, 
	fecha DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id_usuario) REFERENCES "Usuarios" (id), 
	FOREIGN KEY(id_producto) REFERENCES "Producto" (id)
)



CREATE TABLE "Ventas" (
	id INTEGER NOT NULL, 
	id_usuario INTEGER, 
	id_producto INTEGER, 
	"precioVenta" FLOAT NOT NULL, 
	cantidad FLOAT NOT NULL, 
	total FLOAT NOT NULL, 
	fecha DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id_usuario) REFERENCES "Usuarios" (id), 
	FOREIGN KEY(id_producto) REFERENCES "Producto" (id)
)



CREATE TABLE "Inventario" (
	id INTEGER NOT NULL, 
	id_producto INTEGER, 
	cantidad FLOAT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id_producto) REFERENCES "Producto" (id)
)


