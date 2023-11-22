from app.routers.fight import validate_structure
from tests.app.routers.fight.utils import MOVEMENTS_DATA, PLAYER_2_DATA


def test_validate_structure_valid():
    result = validate_structure(MOVEMENTS_DATA)
    assert result.is_ok()


def test_validate_structure_missing_player1():
    movements_data = {
        'player2': PLAYER_2_DATA
    }
    result = validate_structure(movements_data)
    assert result.is_err()
    assert result.err() == 'Las claves "player1" y "player2" son requeridas.'
