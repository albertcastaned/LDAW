from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from punto_venta.models import *
from flask_login import current_user


class RegistarUsuarioForm(FlaskForm):
    
    def validate_username_unico(form, field):
        count = Usuario.query.filter(Usuario.nombre_usuario == form.nombre_usuario.data).first()
        if count:
            raise ValidationError('El nombre de ese usuario ya esta regisrado en el sistema')

    nombre_usuario = StringField('Nombre de Usuario', validators=[DataRequired(message="Llena los datos"), 
        Length(min=5, max=20, message="La longitud del nombre de usuario debe de ser entre 5 a 20 caracteres"), validate_username_unico])

    contrasenia = PasswordField('Contraseña', validators=[DataRequired(message="Llena los datos"), Length(min=5, max=20, message="La longitud del nombre de usuario debe de ser entre 5 a 20 caracteres")])
    confirmar_contrasenia = PasswordField('Confirmar Contraseña', validators=[DataRequired(message="Llena los datos"), EqualTo('contrasenia',message="Ambos campos de contraseña deben ser exactamente igual",), Length(min=5, max=20, message="La longitud del nombre de usuario debe de ser entre 5 a 20 caracteres")])
    
    email = StringField('Correo Electronico', validators=[DataRequired(message="Llena los datos"), Email(message="Correo electronico invalido")])
    nombre_completo = StringField('Nombre Completo', validators=[DataRequired(message="Llena los datos"), Length(min=1, max=120)])
    
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    nombre_usuario = StringField('Nombre de Usuario',
                        validators=[DataRequired()])
    contrasenia = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesion')
