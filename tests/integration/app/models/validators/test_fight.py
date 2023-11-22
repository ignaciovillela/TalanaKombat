from copy import deepcopy

from app.models import MovementsValidator
from tests.utils.utils import (
    MOVEMENTS_DATA, PLAYER_1_HITS_DATA, PLAYER_1_MOVEMENTS_DATA,
)


def test_validate_structure_valid():
    validate_result = MovementsValidator(MOVEMENTS_DATA).validate()
    assert validate_result.is_ok()


def test_validate_structure_missing_player1():
    play_data = deepcopy(MOVEMENTS_DATA)
    play_data.pop('player1')
    validate_result = MovementsValidator(play_data).validate()
    assert validate_result.is_err()
    assert validate_result.err() == ('Las claves "player1" y "player2" son'
                                     ' requeridas.')


def test_validate_play_missing_movements():
    play_data = deepcopy(MOVEMENTS_DATA)
    play_data['player1'].pop('golpes')
    validate_result = MovementsValidator(play_data).validate()
    assert validate_result.is_err()
    assert validate_result.err() == ('Las claves "movimientos" y "golpes" son'
                                     ' requeridas en una jugada.')


def test_validate_play_invalid_movements_length():
    play_data = deepcopy(MOVEMENTS_DATA)
    play_data['player1']['movimientos'] = [*PLAYER_1_MOVEMENTS_DATA, 'Invalid']
    play_data['player1']['golpes'] = [*PLAYER_1_HITS_DATA, 'P']
    validate_result = MovementsValidator(play_data).validate()
    assert validate_result.is_err()
    assert validate_result.err() == ('Cada movimiento debe ser un string de'
                                     ' longitud máxima 5.')
