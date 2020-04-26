from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, NumberRange
from wtforms.widgets import TextArea
from punto_venta.models import *

class RegistarProductoForm(FlaskForm):

    def validate_producto_unico(form, field):
        count = Producto.query.filter(Producto.nombre_producto == form.nombre_producto.data).first()
        if count:
            raise ValidationError('El nombre de ese producto ya se encuentra registrado en el sistema')

    nombre_producto = StringField('Nombre de Producto', validators=[DataRequired(message="Llena los datos"),
        Length(max=150, message="La longitud del nombre de producto debe de ser menor a 50 caracteres"), validate_producto_unico])

    descripcion_producto = StringField('Descripcion de Producto', widget=TextArea(),validators=[
        Length(max=1000, message="La longitud de la descripcion debe ser menos de 1000 caracteres.")])

    marca_producto = StringField('Marca de Producto', validators=[DataRequired(message="Llena los datos"),
        Length(max=150, message="La longitud de la marca de producto debe de ser menor a 150 caracteres")])

    precio_venta = DecimalField('Precio de venta', places=2, validators=[DataRequired(message="El valor debe ser positivo y mayor que 0"), NumberRange(min=0.01, max=None, message="El valor debe ser positivo y mayor que 0")])

    precio_compra = DecimalField('Precio de compra', places=2, validators=[DataRequired(message="El valor debe ser positivo y mayor que 0"), NumberRange(min=0.01, max=None, message="El valor debe ser positivo y mayor que 0")])

    proveedor = StringField('Nombre de Proveedor del producto', validators=[DataRequired(message="Llena los datos"),
        Length(max=150, message="La longitud del proveedor debe de ser menor a 150 caracteres")])

    submit = SubmitField('Registrar')
