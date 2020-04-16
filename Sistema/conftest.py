import os,sys
import pytest

from punto_venta import create_app,db as _db

TESTDB = 'test.db'
TEST_DATABASE_URI = 'sqlite:///' + TESTDB
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Test_Config:
    TESTING= True
    SQLALCHEMY_DATABASE_URI= TEST_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
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

@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""

    def teardown():
        _db.drop_all()

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session
