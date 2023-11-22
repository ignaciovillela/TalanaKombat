from app.use_cases import FightSimulator
from tests.utils.utils import (
    EXPECTED_STORY,
    MOVEMENTS_DATA,
)


def test_narrate_story():
    story = FightSimulator(MOVEMENTS_DATA).narrate_story()
    assert isinstance(story, list)
    assert story == EXPECTED_STORY
