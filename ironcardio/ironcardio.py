from collections import Counter
from random import choices, choice
from rich import print

from dataclasses import dataclass


@dataclass
class Session():
    bells: str
    variation: str
    time: str
    load: str
    swings: str | int


@dataclass
class Loads():
    units: str
    light: int
    medium: int
    heavy: int


BELLS = {"Single Bell": 4 / 6, "Double Bells": 2 / 6}
DOUBLEBELL_VARIATIONS = {
    "Double Classic": 2 / 6,
    "Double Classic + Pullup": 1 / 6,
    "Double Traveling 2s": 2 / 6,
    "SFG II Focus": 1 / 6,
}
SINGLEBELL_VARIATIONS = {
    "Classic": 1 / 6,
    "Classic + Pullup": 1 / 6,
    "Classic + Snatch": 1 / 6,
    "Traveling 2s": 1 / 6,
    "Traveling 2s + Snatch": 1 / 6,
    "Traveling 2s + Pullup": 1 / 6,
}
TIMES = {
    "30 mins": 1 / 6,
    "20 mins": 4 / 6,
    "10 mins": 1 / 6,
}
LOADS = {
    "heavy load": 2 / 6,
    "medium load": 3 / 6,
    "light load": 1 / 6,
}
SWINGS = {True: 2 / 6, False: 4 / 6}


def set_loads():
    """Set the weight for the light, medium, and heavy loads."""
    units = input("[P]ounds or [K]ilograms.").lower()
    if units.startswith() == "p":
        units = "pounds"
    else:
        units = "kilograms"
    light_load = int(input("Enter the weight for the light kettlebells:\n> "))
    medium_load = int(input("Enter the weight for the medium kettlebells:\n> "))
    heavy_load = int(input("Enter the weight for the heavy kettlebells:\n> "))
    return Loads(units, light_load, medium_load, heavy_load)


def create_ic_session():
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
    swings = choices(
        population=tuple(SWINGS.keys()),
        weights=tuple(SWINGS.values()),
    )[0]
    if swings:
        swings = choice(range(50, 110, 10))
    return Session(bells, variation, time, load, swings)


def simulation():
    sessions = [create_ic_session() for s in range(3 * 52)]
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


if __name__ == "__main__":
    session = create_ic_session()
    if session.swings:
        swings = f"Swings: {session.swings} reps"
    else:
        swings = ""
    print(
        f"""Today's Session
    ===============
    Bells: {session.bells.title()}
    Variation: {session.variation}
    Time: {session.time}
    Load: {session.load.title()}
    {swings}
    """
    )
