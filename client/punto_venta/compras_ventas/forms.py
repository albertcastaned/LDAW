from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrarCompra(FlaskForm):
    id_producto = IntegerField('ID Producto', validators=[DataRequired(message="Llena los datos")])

    precio_compra = DecimalField('Precio de compra', places=2, validators=[DataRequired(message="El valor debe ser positivo y mayor que 0"), NumberRange(min=0.01, max=None, message="El valor debe ser positivo y mayor que 0")])
    cantidad = DecimalField('Cantidad', places=2, validators=[DataRequired(message="El valor debe ser positivo y mayor que 0"), NumberRange(min=0.01, max=None, message="El valor debe ser positivo y mayor que 0")])

    submit = SubmitField('Registrar')