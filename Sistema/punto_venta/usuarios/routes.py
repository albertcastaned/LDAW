from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify
from punto_venta.usuarios.forms import *
from punto_venta import API_URL
import requests, json
usuarios = Blueprint('usuarios', __name__, template_folder='templates')

@usuarios.route("/usuarios/registrar", methods=['GET', 'POST'])
def registrar_usuario():
    form = RegistarUsuarioForm()
    if form.validate_on_submit():
        post_data = {
            'nombre_completo':form.nombre_completo.data,
            'nombre_usuario':form.nombre_usuario.data,
            'email':form.email.data,
            'contrasenia':form.contrasenia.data
        }
        response = requests.post(API_URL + "usuarios/registrar/", json = post_data)

        if(response.status_code == 200):
            flash('La cuenta ha sido registrada exitosamente', 'success')
            return redirect(url_for('usuarios.usuarios_lista'))
        else:
            if(response.status_code == 501):
                flash('El nombre de usuario ya existe en el sistema', 'danger')
            else:
                flash('Ocurrio un error desconocido en el sistema', 'danger')

            return render_template('registrar.html', titulo="Registrar Usuario", form=form)
    return render_template('registrar.html', titulo="Registrar Usuario", form=form)


@usuarios.route("/usuarios/", methods=['GET'])
def usuarios_lista():
    page = request.args.get('page', 1, type=int)
    response = requests.get(API_URL + "usuarios/" + str(page))
    return render_template('usuarios_lista.html', usuarios=response.json(), titulo="Lista de Usuarios")
'''

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
            flash('Ha iniciado sesion exitosamente', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Inicio de Sesion no fue exitoso. Verifica los campos', 'danger')
    return render_template('login.html', titulo='Iniciar Sesion', form=form)

@usuarios.route("/usuarios/logout")
def logout():
    logout_user()
    flash('Ha cerrado sesion exitosamente', 'success')
    return redirect(url_for('usuarios.login'))
'''