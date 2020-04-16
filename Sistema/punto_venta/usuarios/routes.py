from flask import render_template, url_for, flash, redirect, request, Blueprint
from punto_venta.usuarios.forms import *
from punto_venta.models import Usuario
from punto_venta import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

usuarios = Blueprint('usuarios', __name__, template_folder='templates')

@usuarios.route("/usuarios/registrar", methods=['GET', 'POST'])
def registrar_usuario():
    form = RegistarUsuarioForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.contrasenia.data).decode('utf-8')
        usuario = Usuario(nombre_usuario=form.nombre_usuario.data, email=form.email.data, contrasenia=hashed_password, nombre_completo=form.nombre_completo.data)
        db.session.add(usuario)
        db.session.commit()
        print("Nuevo Usuario Creado")
        flash('La cuenta ha sido registrada exitosamente', 'success')
        return redirect(url_for('usuarios.usuarios_lista'))
    return render_template('registrar.html', titulo="Registrar Usuario", form=form)

@usuarios.route("/usuarios/", methods=['GET'])
def usuarios_lista():
    page = request.args.get('pagina', 1, type=int)
    usuarios = Usuario.query.paginate(page=page, per_page=10)
    return render_template('usuarios_lista.html', usuarios=usuarios, titulo="Lista de Usuarios")

@usuarios.route("/usuarios/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(nombre_usuario=form.nombre_usuario.data).first()
        if user and bcrypt.check_password_hash(user.contrasenia, form.contrasenia.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Inicio de Sesion no fue exitoso. Verifica los campos', 'danger')
    return render_template('login.html', titulo='Iniciar Sesion', form=form)

@usuarios.route("/usuarios/logout")
def logout():
    logout_user()
    return redirect(url_for('usuarios.login'))