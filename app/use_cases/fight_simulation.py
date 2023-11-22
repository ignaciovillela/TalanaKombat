from typing import List, Tuple

from app.models import Player
from app.typings import MovementsTyping


class StoryException(Exception):
    """Custom exception for story-related errors."""


class FightSimulator:

    def __init__(self, movements: MovementsTyping):
        self._story = []
        self._players = self._get_players_ordered(movements)

    def narrate_story(self) -> List[str]:
        """Narrates the story of the fight based on the provided movements."""
        player, opponent = self._players

        while player.energy > 0 and opponent.energy > 0:
            try:
                self._simulate_round(player, opponent)
            except StoryException:
                break
            player, opponent = self._switch_players(player, opponent)

        return self._story

    def _get_players_ordered(self, movements: MovementsTyping) -> List[Player]:
        """Gets the players in order based on combined lengths of movements and
            hits."""
        player_1_data = movements['player1']
        player_2_data = movements['player2']

        player_1 = Player('player1',
                          player_1_data['movimientos'],
                          player_1_data['golpes'])
        player_2 = Player('player2',
                          player_2_data['movimientos'],
                          player_2_data['golpes'])

        players = [player_1, player_2]
        players.sort(key=self._calculate_combined_lengths)

        return players

    @staticmethod
    def _calculate_combined_lengths(player: Player) -> Tuple[int, int, int]:
        """Calculates the combined lengths of movements and hits for a
            player."""
        movements_length = len(''.join(player.movements))
        hits_length = len(''.join(player.hits))
        total_length = movements_length + hits_length
        return total_length, movements_length, hits_length

    def _simulate_round(self, player: Player, opponent: Player) -> None:
        """Simulates a round in the fight and updates the story."""
        try:
            movement = next(player.movements_generator)
        except StopIteration as exception:
            self._story.append(f'{player.short_name} se ha quedado sin'
                               f' movimientos. La pelea ha finalizado.')
            raise StoryException(exception) from exception

        self._story.append(movement.get_movement_text(player, opponent))
        movement.hit(opponent=opponent)

        if opponent.energy <= 0:
            self._story.append(f'{player.short_name} Gana la pelea y aún le'
                               f' queda {player.energy} de energía')

    @staticmethod
    def _switch_players(player: Player, opponent: Player) \
            -> Tuple[Player, Player]:
        """Switches the current player and opponent."""
        return opponent, player
