from app.routers.fight import validate_play
from tests.app.routers.fight.utils import (
    PLAYER_1_DATA, PLAYER_1_HITS_DATA,
    PLAYER_1_MOVEMENTS_DATA,
)


def test_validate_play_valid():
    play_data = PLAYER_1_DATA
    result = validate_play(play_data)
    assert result.is_ok()


def test_validate_play_missing_movements():
    play_data = {'golpes': PLAYER_1_HITS_DATA}
    result = validate_play(play_data)
    assert result.is_err()
    assert result.err() == 'Las claves "movimientos" y "golpes" son requeridas en una jugada.'


def test_validate_play_invalid_movements_length():
    play_data = {
        'movimientos': [*PLAYER_1_MOVEMENTS_DATA, 'Invalid'],
        'golpes': PLAYER_1_HITS_DATA,
    }
    result = validate_play(play_data)
    assert result.is_err()
    assert result.err() == 'Cada movimiento debe ser un string de longitud máxima 5.'
