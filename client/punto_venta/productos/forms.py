from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, NumberRange, Regexp
from wtforms.widgets import TextArea

class RegistarProductoForm(FlaskForm):


    nombre_producto = StringField('Nombre de Producto', validators=[DataRequired(message="Llena los datos"),
        Length(max=150, message="La longitud del nombre de producto debe de ser menor a 50 carácteres"),
        Regexp(r'^[\w.]+$')
        ])

    descripcion_producto = StringField('Descripción del Producto', widget=TextArea(),validators=[
        Length(max=1000, message="La longitud de la descripcion debe ser menos de 1000 carácteres.",),
        Regexp(r'^[\w.]+$')
        ])

    marca_producto = StringField('Marca de Producto', validators=[DataRequired(message="Llena los datos"),
        Length(max=150, message="La longitud de la marca de producto debe de ser menor a 150 carácteres")])

    precio_venta = DecimalField('Precio de Venta', places=2, validators=[DataRequired(message="El valor debe ser positivo y mayor que 0"), NumberRange(min=0.01, max=None, message="El valor debe ser positivo y mayor que 0")])

    precio_compra = DecimalField('Precio de Compra', places=2, validators=[DataRequired(message="El valor debe ser positivo y mayor que 0"), NumberRange(min=0.01, max=None, message="El valor debe ser positivo y mayor que 0")])

    proveedor = StringField('Proveedor', validators=[DataRequired(message="Llena los datos"),
        Length(max=150, message="La longitud del proveedor debe de ser menor a 150 carácteres"),
        Regexp(r'^[\w.]+$')])

    submit = SubmitField('Registrar')
