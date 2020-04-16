from flask import render_template, url_for, flash, redirect, request, Blueprint
from punto_venta.usuarios.forms import RegistarUsuarioForm
from punto_venta.models import Usuario
from punto_venta import db, bcrypt

usuarios = Blueprint('usuarios', __name__, template_folder='templates')

@usuarios.route("/usuarios/registrar", methods=['GET', 'POST'])
def registrar_usuario():
    form = RegistarUsuarioForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.contrasenia.data).decode('utf-8')
        usuario = Usuario(nombre_usuario=form.nombre_usuario.data, email=form.email.data, contrasenia=hashed_password, nombre_completo=form.nombre_completo.data)
        db.session.add(usuario)
        db.session.commit()
        flash('La cuenta ha sido registrada exitosamente', 'success')
        return redirect(url_for('usuarios.usuarios_lista'))
    return render_template('registrar.html', titulo="Registrar Usuario", form=form)

@usuarios.route("/usuarios/", methods=['GET'])
def usuarios_lista():
    page = request.args.get('pagina', 1, type=int)
    usuarios = Usuario.query.paginate(page=page, per_page=10)
    return render_template('usuarios_lista.html', usuarios=usuarios, titulo="Lista de Usuarios")