from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_redirect():
    response = client.get('/')
    assert response.url == 'http://testserver/kombat/'


def test_kombat_route():
    response = client.get('/kombat/')
    assert response.status_code == 200
    assert response.json() == {
        'info': 'Bienvenido a la API de Talana Kombat! Para iniciar una pelea,'
                ' envía una solicitud POST a la URL /kombat/fight.'}


def test_invalid_route():
    response = client.get('/invalid-route/')
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
