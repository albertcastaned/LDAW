import os,sys
import pytest

from punto_venta import create_app

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Test_Config:
    TESTING= True
    WTF_CSRF_ENABLED= False
    WTF_CSRF_METHODS= []
    SECRET_KEY = os.urandom(24)

@pytest.fixture(scope='session')
def app(request):

    app = create_app(Test_Config)
    
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()
