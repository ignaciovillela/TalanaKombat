from result import Err, Ok, Result

from app.typings import MovementsTyping, PlayerTyping


class MovementsValidator:

    def __init__(self, movements: MovementsTyping):
        self.movements = movements

    def validate(self) -> Result:
        """Validates the structure of the movements JSON.

        Returns:
            Result: Result containing None for success or an error message.
        """
        # Check that keys 'player1' and 'player2' are present
        if 'player1' not in self.movements or 'player2' not in self.movements:
            return Err('Las claves "player1" y "player2" son requeridas.')

        # Validate the structure of 'player1'
        player1_result = self._validate_play(self.movements['player1'])
        if player1_result.is_err():
            return player1_result

        # Validate the structure of 'player2'
        player2_result = self._validate_play(self.movements['player2'])
        if player2_result.is_err():
            return player2_result

        return Ok(None)

    @staticmethod
    def _validate_play(play: PlayerTyping) -> Result:
        """Validates the structure of a player's movements.

        Args:
            play (PlayerTyping): The player's movements.

        Returns:
            Result: Result containing None for success or an error message.
        """
        # Check that keys 'movimientos' and 'golpes' are present
        if 'movimientos' not in play or 'golpes' not in play:
            return Err('Las claves "movimientos" y "golpes" son requeridas en'
                       ' una jugada.')

        # Validate the length of 'movimientos' and 'golpes'
        if len(play['movimientos']) != len(play['golpes']):
            return Err('Para cada jugador, la cantidad de movimientos y de'
                       ' golpes debe ser la misma.')

        # Validate the length of 'movimientos'
        for movement in play['movimientos']:
            if not isinstance(movement, str) or len(movement) > 5:
                return Err('Cada movimiento debe ser un string de longitud'
                           ' máxima 5.')

        # Validate the length of 'golpes'
        for hit in play['golpes']:
            if not isinstance(hit, str) or len(hit) > 1:
                return Err('Cada golpe debe ser un string de longitud máxima'
                           ' 1.')

        return Ok(None)
