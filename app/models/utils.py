"""Utility Functions.

This module provides utility functions for the models.
"""


def get_movement_name(movement: str, player_number: int) -> str:
    """Gets the name of the movement based on the movement string and player
        number.

    Args:
        movement (str): The movement string.
        player_number (int): The player number.

    Returns:
        str: The name of the movement.
    """
    movement = movement[:1].upper()
    if movement == 'W':
        return 'sube'
    if movement == 'S':
        return 'baja'
    if (movement, player_number) in (('A', 1), ('D', 2)):
        return 'retrocede'
    return 'avanza'
