import sys, os, tempfile
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from api import app_api
import pytest

@pytest.fixture
def client():
    db_fd, app_api.app.config['SQLALCHEMY_DATABASE_URI'] = tempfile.mkstemp()
    app_api.app.config['TESTING'] = True

    with app_api.app.test_client() as client:
        with app_api.app.app_context():
            app_api.init_db()
        yield client

    os.close(db_fd)
    os.unlink(app_api.app.config['SQLALCHEMY_DATABASE_URI'])

def test_obtener_usuarios(client, session):
    resp = client.get("/api/v1/usuarios/1/")
    assert resp.status_code == 200