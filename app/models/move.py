"""Move Models.

This module defines the movement classes for the game.
"""

from .utils import get_movement_name


class BaseMovement:
    """Base class for generic movements.

    Attributes:
        name (str): The name of the movement.
        prefix (str): The prefix used in the movement text.
        combination (str): The combination of the movement.
        power (int): The power or energy impact of the movement.
        pre_movements (str): The movements that precede the current movement.

    Methods:
        check_combination(cls, movement, hit): Checks if the given movement and
            hit form the combination.
        _get_pre_movements(self, movements): Gets the movements that precede
            the current movement.
        hit(self, opponent): Applies the impact of the movement on the
            opponent.
        get_action(self): Returns the action description of the movement.
        get_movement_text(self, player, opponent): Generates the text
            description of the movement in the fight.
    """
    name = ''
    prefix = ''
    combination = ''
    power = 0

    pre_movements = ''

    def __init__(self, movements: str = ''):
        self.pre_movements = self._get_pre_movements(movements)

    @classmethod
    def check_combination(cls, movement: str, hit: str) -> bool:
        """Checks if the given movement and hit form the combination.

        Args:
            movement (str): The movement string.
            hit (str): The hit string.

        Returns:
            bool: True if the combination is valid, False otherwise.
        """
        full_movement = f'{movement}+{hit}'
        return full_movement.upper().endswith(cls.combination.upper())

    def _get_pre_movements(self, movements: str) -> str:
        """Gets the movements that precede the current movement.

        Args:
            movements (str): The movements string.

        Returns:
            str: The movements that precede the current movement.
        """
        if '+' not in self.combination:
            return movements
        combination_movements = self.combination.split('+')
        movement_len = len(combination_movements)
        return movements[:-movement_len]

    def hit(self, opponent: 'Player') -> None:
        """Applies the impact of the movement on the opponent.

        Args:
            opponent (Player): The opponent player.
        """
        opponent.energy -= self.power

    def _get_action(self) -> str:
        return f'{self.prefix} {self.name}'.strip()

    def get_movement_text(self, player: 'Player', opponent: 'Player') -> str:
        """Generates the text description of the movement in the fight.

        Args:
            player (Player): The player performing the movement.
            opponent (Player): The opponent player.

        Returns:
            str: The text description of the movement in the fight.
        """
        text_list = [player.short_name]
        if self.pre_movements:
            movement_name = get_movement_name(
                self.pre_movements, player.player_number)
            text_list.append(movement_name)

        if action := self._get_action():
            if self.pre_movements:
                text_list.append('y')
            text_list.append(action)

        if (self.combination
                and opponent.energy <= opponent.__class__.energy / 2):
            text_list.append(opponent.fight_name)

        return ' '.join(text_list)


class SpecialMovementMixin:
    """Mixin class for special movements.

    Methods:
        _get_pre_movements(self, movements): Overrides the method to return an
            empty string.
    """

    def _get_pre_movements(self, movements: str) -> str:
        """Overrides the method to return an empty string.

        Args:
            movements (str): The movements string.

        Returns:
            str: An empty string.
        """
        return ''


class Punch(BaseMovement):
    name = 'puñetazo'
    prefix = 'da un'
    combination = 'P'
    power = 1


class Kick(BaseMovement):
    name = 'patada'
    prefix = 'da una'
    combination = 'K'
    power = 1


class TonynTaladoken(SpecialMovementMixin, BaseMovement):
    name = 'Taladoken'
    prefix = 'usa un'
    combination = 'DSD+P'
    power = 3


class TonynRemuyuken(SpecialMovementMixin, BaseMovement):
    name = 'Remuyuken'
    prefix = 'conecta un'
    combination = 'SD+K'
    power = 2


class ArnaldorRemuyuken(SpecialMovementMixin, BaseMovement):
    name = 'Remuyuken'
    prefix = 'conecta un'
    combination = 'SA+K'
    power = 3


class ArnaldorTaladoken(SpecialMovementMixin, BaseMovement):
    name = 'Taladoken'
    prefix = 'da un'
    combination = 'ASA+P'
    power = 2
