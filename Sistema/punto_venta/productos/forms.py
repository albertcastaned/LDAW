from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from punto_venta.models import *

class RegistarProductoForm(FlaskForm):

    def validate_producto_unico(form, field):
        count = Producto.query.filter(Producto.nombre_producto == form.nombre_producto.data).first()
        if count:
            raise ValidationError('El nombre de ese producto ya se encuentra registrado en el sistema')

    nombre_producto = StringField('Nombre de Producto', validators=[DataRequired(message="Llena los datos"),
        Length(min=5, max=50, message="La longitud del nombre de producto debe de ser entre 5 a 50 caracteres"), validate_producto_unico])

    descripcion_producto = StringField('Descripcion de Producto', validators=[DataRequired(message="Llena los datos"),
        Length(min=5, max=500, message="Porfavor ingresa una descripcion del producto.")])

    marca_producto = StringField('Marca de Producto', validators=[DataRequired(message="Llena los datos"),
        Length(min=5, max=50, message="La longitud de la marca de producto debe de ser entre 5 a 50 caracteres")])

    precio_venta = DecimalField('Precio de venta', places=2, validators=[DataRequired(message="Llena los datos")])

    precio_compra = DecimalField('Precio de compra', places=2, validators=[DataRequired(message="Llena los datos")])

    proveedor = StringField('Nombre de Proveedor del producto', validators=[DataRequired(message="Llena los datos"),
        Length(min=5, max=500, message="Porfavor ingresa el nombre del proveedor del producto.")])

    submit = SubmitField('Registrar')
