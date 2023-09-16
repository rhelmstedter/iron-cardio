from pathlib import Path
import json

from iron_cardio.constants import (
    BELLS,
    DOUBLEBELL_VARIATIONS,
    SINGLEBELL_VARIATIONS,
    TIMES,
)
from iron_cardio.iron_cardio import Session, create_session, display_session
from .test_constants import TEST_SESSION

POSSIBLE_SWINGS = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]


def test_create_session(database):
    loads = json.load(open(database.name))['loads']
    actual = create_session(Path(database.name))
    assert isinstance(actual, Session)
    assert actual.bells in BELLS.keys()
    assert (
        actual.variation in DOUBLEBELL_VARIATIONS.keys()
        or actual.variation in SINGLEBELL_VARIATIONS.keys()
    )
    assert actual.time in TIMES.keys()
    assert actual.load in loads.values()
    assert actual.units == loads['units']
    assert actual.swings is False or actual.swings in POSSIBLE_SWINGS


def test_display_session(capfd):
    display_session(TEST_SESSION)
    output = capfd.readouterr()[0]
    assert "Iron Cardio Session" in output
    assert "====================" in output
    assert "Bells: " in output
    assert "Variation: " in output
    assert "Time: " in output
    assert "Load: " in output
