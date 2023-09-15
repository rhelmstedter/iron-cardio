from iron_cardio.iron_cardio import create_session, Session
from iron_cardio.constants import (
    BELLS,
    DOUBLEBELL_VARIATIONS,
    SINGLEBELL_VARIATIONS,
    TIMES,
    IRON_CARDIO_DB,
)

POSSIBLE_SWINGS = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]


def test_create_session():
    actual = create_session(IRON_CARDIO_DB)
    assert isinstance(actual, Session)
    assert actual.bells in BELLS.keys()
    assert (
        actual.variation in DOUBLEBELL_VARIATIONS.keys()
        or actual.variation in SINGLEBELL_VARIATIONS.keys()
    )
    assert actual.time in TIMES.keys()
    assert actual.swings is False or actual.swings in POSSIBLE_SWINGS
