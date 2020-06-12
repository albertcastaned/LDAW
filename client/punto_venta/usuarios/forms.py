from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class RegistarUsuarioForm(FlaskForm):
    nombre_usuario = StringField('Nombre de Usuario', validators=[DataRequired(message="Llena los datos"), 
        Length(min=5, max=20, message="La longitud del nombre de usuario debe de ser entre 5 a 20 carácteres")])

    contrasenia = PasswordField('Contraseña', validators=[DataRequired(message="Llena los datos"), Length(min=5, max=20, message="La longitud del nombre de usuario debe de ser entre 5 a 20 carácteres")])
    confirmar_contrasenia = PasswordField('Confirmar Contraseña', validators=[DataRequired(message="Llena los datos"), EqualTo('contrasenia',message="Ambos campos de contraseña deben ser exactamente igual",), Length(min=5, max=20, message="La longitud del nombre de usuario debe de ser entre 5 a 20 caracteres")])
    
    email = StringField('Correo Electrónico', validators=[DataRequired(message="Llena los datos"), Email(message="Correo electrónico inválido")])
    nombre_completo = StringField('Nombre Completo', validators=[DataRequired(message="Llena los datos"), Length(min=1, max=120)])
    roles = MultiCheckboxField("Roles", coerce=int,validators=[DataRequired(message="Selecciona por lo menos un rol")])
    
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    nombre_usuario = StringField('Nombre de Usuario',
                        validators=[DataRequired()])
    contrasenia = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')
