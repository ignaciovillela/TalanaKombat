from fastapi.testclient import TestClient

from app.main import app
from tests.app.routers.fight.utils import MOVEMENTS_DATA

client = TestClient(app)


def test_simulate_fight():
    response = client.post('/kombat/fight', json=MOVEMENTS_DATA)
    assert response.status_code == 200
    assert 'story' in response.json()
    assert 'story_text' in response.json()
