"""Router for simulating fights in the game.

This module defines the FastAPI router for simulating fights.
"""

from typing import Dict, Tuple
from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from result import Err, Ok, Result

from models import Player

PlayerTyping = Dict[str, List[str]]
MovementsTyping = Dict[str, PlayerTyping]

router = APIRouter()


# region Validations


def validate_structure(movements: MovementsTyping) -> Result:
    """Validates the structure of the movements JSON.

    Args:
        movements (MovementsTyping): The movements JSON.

    Raises:
        HTTPException: If the structure is invalid.
    """
    # Check that keys 'player1' and 'player2' are present
    if 'player1' not in movements or 'player2' not in movements:
        return Err('Las claves "player1" y "player2" son requeridas.')

    # Validate the structure of 'player1'
    player1_result = validate_play(movements['player1'])
    if player1_result.is_err():
        return player1_result

    # Validate the structure of 'player2'
    player2_result = validate_play(movements['player2'])
    if player2_result.is_err():
        return player2_result

    return Ok(None)


def validate_play(play: PlayerTyping) -> Result:
    """Validates the structure of a player's movements.

    Args:
        play (PlayerTyping): The player's movements.

    Raises:
        HTTPException: If the structure is invalid.
    """
    # Check that keys 'movimientos' and 'golpes' are present
    if 'movimientos' not in play or 'golpes' not in play:
        return Err('Las claves "movimientos" y "golpes" son requeridas en'
                   ' una jugada.')

    # Validate the length of 'movimientos' and 'golpes'
    if len(play['movimientos']) != len(play['golpes']):
        return Err('Para cada jugador, la cantidad de movimientos y de golpes'
                   ' debe ser la misma.')

    # Validate the length of 'movimientos'
    for movement in play['movimientos']:
        if not isinstance(movement, str) or len(movement) > 5:
            return Err('Cada movimiento debe ser un string de longitud máxima 5.')

    # Validate the length of 'golpes'
    for hit in play['golpes']:
        if not isinstance(hit, str) or len(hit) > 1:
            return Err('Cada golpe debe ser un string de longitud máxima 1.')

    return Ok(None)


# endregion

# region Narration


class StoryException(Exception):
    """Custom exception for story-related errors."""


def calculate_combined_lengths(player: Player) -> Tuple[int, int, int]:
    """Calculates the combined lengths of movements and hits for a player.

    Args:
        player (Player): The player.

    Returns:
        Tuple[int, int, int]: The total length, movements length, and hits
            length.
    """
    movements_length = len(''.join(player.movements))
    hits_length = len(''.join(player.hits))
    total_length = movements_length + hits_length
    return total_length, movements_length, hits_length


def get_players_ordered(movements: MovementsTyping) -> List[Player]:
    """Gets the players in order based on combined lengths of movements and
        hits.

    Args:
        movements (MovementsTyping): The movements JSON.

    Returns:
        List[Player]: The ordered list of players.
    """
    player_1_data = movements['player1']
    player_2_data = movements['player2']

    player_1 = Player('player1', player_1_data['movimientos'], player_1_data['golpes'])
    player_2 = Player('player2', player_2_data['movimientos'], player_2_data['golpes'])

    players = [player_1, player_2]
    players.sort(key=calculate_combined_lengths)

    return players


def simulate_round(story: List[str], player: Player, opponent: Player) -> None:
    """Simulates a round in the fight and updates the story.

    Args:
        story (List[str]): The ongoing story.
        player (Player): The player whose turn it is.
        opponent (Player): The opponent player.

    Raises:
        StoryException: If the player has no movements left.
    """
    try:
        movement = next(player.movements_generator)
    except StopIteration as exception:
        story.append(f'{player.short_name} se ha quedado sin movimientos.'
                     f' La pelea ha finalizado.')
        raise StoryException(exception) from exception

    story.append(movement.get_movement_text(player, opponent))
    movement.hit(opponent=opponent)

    if opponent.energy <= 0:
        story.append(f'{player.short_name} Gana la pelea y aún le queda '
                     f'{player.energy} de energía')


def narrate_story(movements: MovementsTyping) -> List[str]:
    """Narrates the story of the fight based on the provided movements.

    Args:
        movements (MovementsTyping): The movements JSON.

    Returns:
        List[str]: The story of the fight.
    """
    story = []
    player, opponent = get_players_ordered(movements)
    while player.energy > 0 and opponent.energy > 0:
        try:
            simulate_round(story, player, opponent)
        except StoryException:
            break
        player, opponent = opponent, player

    return story


# endregion

# region Routers


# Define a root route to provide information
@router.get('/')
def root():
    """
    Provides information about the API.

    Returns:
        dict: A dictionary with information about the API usage.
    """
    return {'info': 'Bienvenido a la API de Kombat! Para iniciar una pelea,'
                    ' envía una solicitud POST a la URL /kombat/fight.'}


@router.get('/fight')
def simulate_fight_info():
    """
    Provides information about the API.

    Returns:
        dict: A dictionary with information about the API usage.
    """
    return {'info': 'Genial, has llegado a la URL! Para iniciar una pelea,'
                    ' envía una solicitud POST.'}


@router.post('/fight')
def simulate_fight(movements: MovementsTyping):
    """Simulates a fight and returns the narration.

    Args:
        movements (MovementsTyping): Movements of the players.

    Returns:
        Dict[str, Union[List[str], str]]: A dictionary containing the story
            as a list of events and consolidated text.
    """
    validate_result = validate_structure(movements)
    if validate_result.is_err():
        raise HTTPException(status_code=400, detail=f'Error: {validate_result.err()}')

    story = narrate_story(movements)
    return {'story': story, 'story_text': '\n'.join(story)}


# endregion
