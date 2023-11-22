"""Router for simulating fights in the game.

This module defines the FastAPI router for simulating fights.
"""

from typing import Dict

from fastapi import APIRouter, HTTPException

from app.models import MovementsValidator
from app.typings import MovementsTyping
from app.use_cases.fight_simulation import FightSimulator

router = APIRouter()


# Define a root route to provide information
@router.get('/')
def root():
    """
    Provides information about the API.

    Returns:
        dict: A dictionary with information about the API usage.
    """
    return {'info': 'Bienvenido a la API de Talana Kombat! Para iniciar una'
                    ' pelea, envía una solicitud POST a la URL /kombat/fight.'}


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
    validate_result = MovementsValidator(movements).validate()
    if validate_result.is_err():
        raise HTTPException(status_code=400,
                            detail=f'Error: {validate_result.err()}')

    story = FightSimulator(movements).narrate_story()
    return {'story': story, 'story_text': '\n'.join(story)}
