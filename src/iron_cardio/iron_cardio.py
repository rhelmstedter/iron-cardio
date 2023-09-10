from collections import Counter
import json
from random import choices, choice
from rich import print

from dataclasses import dataclass
from .constants import (
    BELLS,
    DOUBLEBELL_VARIATIONS,
    SINGLEBELL_VARIATIONS,
    TIMES,
    LOADS,
    SWINGS,
    IRON_CARDIO_DB,
)


@dataclass
class Session:
    bells: str
    variation: str
    time: str
    load: str
    units: str
    swings: bool | int


def create_session():
    with open(IRON_CARDIO_DB, "r") as db:
        data = json.load(db)
        loads = data["loads"]
    bells = choices(
        population=tuple(BELLS.keys()),
        weights=tuple(BELLS.values()),
    )[0]
    if bells == "Double Bells":
        variation = choices(
            population=tuple(DOUBLEBELL_VARIATIONS.keys()),
            weights=tuple(DOUBLEBELL_VARIATIONS.values()),
        )[0]
    elif bells == "Single Bell":
        variation = choices(
            population=tuple(SINGLEBELL_VARIATIONS.keys()),
            weights=tuple(SINGLEBELL_VARIATIONS.values()),
        )[0]
    time = choices(
        population=tuple(TIMES.keys()),
        weights=tuple(TIMES.values()),
    )[0]
    load = choices(
        population=tuple(LOADS.keys()),
        weights=tuple(LOADS.values()),
    )[0]
    load = loads[load]
    units = loads["units"]
    swings = choices(
        population=tuple(SWINGS.keys()),
        weights=tuple(SWINGS.values()),
    )[0]
    if swings:
        swings = choice(range(50, 110, 10))
    return Session(bells, variation, time, load, units, swings)


def display_session(session: Session) -> None:
    if session.swings:
        swings = f"Swings: {session.swings} reps"
    else:
        swings = ""
    print(
        f"""Iron Cardio Session
    ===============
    Bells: {session.bells.title()}
    Variation: {session.variation}
    Time: {session.time}
    Load: {session.load} {session.units}
    {swings}
    """
    )

def simulation():
    sessions = [create_session() for s in range(3 * 52)]
    stats = Counter()
    for session in sessions:
        for c in session:
            if isinstance(c, int):
                c = "Swings"
            stats.update([c])
    one_year = dict(sorted(stats.items(), key=lambda x: x[1], reverse=True))
    width = len(max(one_year.keys(), key=len))
    for session, count in one_year.items():
        print(f"{session: >{width}}: " + "#" * count)
        print(f"{session: >{width}}: " + "#" * count)
