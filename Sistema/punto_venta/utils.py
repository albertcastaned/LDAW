from flask import url_for, redirect, session, request
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('usuarios.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
