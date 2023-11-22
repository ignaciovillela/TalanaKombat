
PLAYER_1_MOVEMENTS_DATA = ['D', 'DSD', 'S', 'DSD', 'SD']
PLAYER_1_HITS_DATA = ['K', 'P', '', 'K', 'P']
PLAYER_1_DATA = {
    'movimientos': PLAYER_1_MOVEMENTS_DATA,
    'golpes': PLAYER_1_HITS_DATA,
}

PLAYER_2_MOVEMENTS_DATA = ['SA', 'SA', 'SA', 'ASA', 'SA']
PLAYER_2_HITS_DATA = ['K', '', 'K', 'P', 'P']
PLAYER_2_DATA = {
    'movimientos': PLAYER_2_MOVEMENTS_DATA,
    'golpes': PLAYER_2_HITS_DATA,
}

MOVEMENTS_DATA = {
    'player1': PLAYER_1_DATA,
    'player2': PLAYER_2_DATA,
}

EXPECTED_STORY = [
    'Tonyn avanza y da una patada',
    'Arnaldor conecta un Remuyuken',
    'Tonyn usa un Taladoken',
    'Arnaldor baja',
    'Tonyn baja',
    'Arnaldor conecta un Remuyuken al pobre Tonyn',
    'Arnaldor Gana la pelea y aún le queda 2 de energía',
]
