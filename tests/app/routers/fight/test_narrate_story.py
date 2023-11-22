from app.routers.fight import narrate_story
from tests.app.routers.fight.utils import MOVEMENTS_DATA


def test_narrate_story():
    expected_story = [
        'Tonyn avanza y da una patada',
        'Arnaldor conecta un Remuyuken',
        'Tonyn usa un Taladoken',
        'Arnaldor baja',
        'Tonyn baja',
        'Arnaldor conecta un Remuyuken al pobre Tonyn',
        'Arnaldor Gana la pelea y aún le queda 2 de energía',
    ]

    story = narrate_story(MOVEMENTS_DATA)
    assert isinstance(story, list)
    assert story == expected_story
