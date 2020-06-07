from flask import url_for, redirect, session, request, abort
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('usuarios.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def is_administrator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'roles' in session:
            for rol in session['roles']:
                if rol['nombre'].lower() == "Administrador".lower():
                    return f(*args, **kwargs)
        abort(403, "No tiene permiso para acceder a esta pagina.")
    return decorated_function

def is_gerente(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'roles' in session:
            for rol in session['roles']:
                if rol['nombre'].lower() == "Gerente".lower():
                    return f(*args, **kwargs)
        abort(403, "No tiene permiso para acceder a esta pagina.")
    return decorated_function

def is_asistente(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'roles' in session:
            for rol in session['roles']:
                if rol['nombre'].lower() == "Asistente".lower():
                    return f(*args, **kwargs)
        abort(403, "No tiene permiso para acceder a esta pagina.")
    return decorated_function