"""Player Models for the game.

This module defines the Player class and its subclasses.
"""

from typing import Iterator, List

from .move import (
    ArnaldorRemuyuken, ArnaldorTaladoken,
    BaseMovement, Kick, Punch, TonynRemuyuken, TonynTaladoken,
)


class Player:
    """Base class for players in the game.

    Attributes:
        pk (str): The name of the player.
        name (str): The default name of the player.
        energy (int): The energy level of the player.
        movements (list): A list of available movements for the player.

    Methods:
        __new__(cls, name): Creates a new instance of the Player class based
            on the player name.
        __init_subclass__(cls): Registers subclasses in the __players
            dictionary.
        short_name (property): Returns the short name of the player.
    """

    pk = None
    __players = {}

    name = 'Jugador'
    energy = 6
    player_number = 1
    plays = [
        Punch,
        Kick,
    ]

    def __new__(cls, pk: str, movements: List[str], hits: List[str]):
        target_class = cls.__players.get(pk, cls)
        obj = super().__new__(target_class)
        return obj

    def __init__(self, pk: str, movements: List[str], hits: List[str]):
        self.movements = movements
        self.hits = hits
        self.movements_generator = self._get_movements()

    def __init_subclass__(cls):
        cls.__players[cls.pk] = cls

    def _get_movements(self) -> Iterator[BaseMovement]:
        for movement, hit in zip(self.movements, self.hits):
            yield self._get_movement(movement, hit)

    def _get_movement(self, movement: str, hit: str) -> BaseMovement:
        best_play = BaseMovement(movement)
        for play_class in self.plays:
            play = play_class(movement)
            if (play.check_combination(movement, hit)
                    and len(play.combination) > len(best_play.combination)):
                best_play = play
        return best_play

    @property
    def short_name(self) -> str:
        """Returns the fight first name."""
        return self.name.split()[0]

    @property
    def fight_name(self) -> str:
        """Returns the fight name based on the player's energy."""
        if self.energy <= self.__class__.energy / 2:
            return f'al pobre {self.short_name}'
        return ''


class Tonyn(Player):
    pk = 'player1'
    name = 'Tonyn Stallone'
    plays = Player.plays + [
        TonynTaladoken,
        TonynRemuyuken,
    ]


class Arnaldor(Player):
    pk = 'player2'
    name = 'Arnaldor Shuatseneguer'
    player_number = 2
    plays = Player.plays + [
        ArnaldorRemuyuken,
        ArnaldorTaladoken,
    ]
