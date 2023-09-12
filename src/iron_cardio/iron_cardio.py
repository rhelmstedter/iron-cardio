import json
from collections import Counter
from dataclasses import dataclass
from random import choice, choices

from rich import print
from rich.console import Console
from rich.prompt import Confirm, IntPrompt, Prompt

from .constants import (
    BELLS,
    DOUBLEBELL_VARIATIONS,
    IRON_CARDIO_DB,
    LOADS,
    SINGLEBELL_VARIATIONS,
    SWINGS,
    TIMES,
)


@dataclass
class Session:
    bells: str
    variation: str
    time: str
    load: str
    units: str
    swings: bool | int
    sets: int = 0


console = Console()


def create_session():
    with open(IRON_CARDIO_DB) as db:
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
        swings = choice(range(50, 160, 10))
    return Session(bells, variation, time, load, units, swings)


def _get_options(session_param: dict) -> str:
    """Select options for a given Session parameter."""
    options = list(session_param.keys())
    for i, option in enumerate(options, 1):
        print(f"    [{i}] {option}")
    selection = IntPrompt.ask("Choose your option")
    return options[selection - 1]


def create_custom_session():
    """Create a custom Iron Cardio session."""
    bells = _get_options(BELLS)
    if bells == "Double Bells":
        variation = _get_options(DOUBLEBELL_VARIATIONS)
    elif bells == "Single Bell":
        variation = _get_options(SINGLEBELL_VARIATIONS)
    time = IntPrompt.ask("How long was your session (in minutes)")
    units = _get_units()
    load = IntPrompt.ask(f"What weight did you use (in {units})")
    if Confirm.ask("Did you swing"):
        swings = IntPrompt.ask("How many swings")
    return Session(bells, variation, time, load, units, swings)


def display_session(session: Session) -> None:
    if session.swings:
        swings = f"Swings: {session.swings} reps"
    else:
        swings = ""
    print(
        f"""Iron Cardio Session
    ====================
    Bells: {session.bells.title()}
    Variation: {session.variation}
    Time: {session.time}
    Load: {session.load} {session.units}
    {swings}
    """
    )


def _get_units():
    while True:
        units = Prompt.ask("[P]ounds or [K]ilograms").lower()
        if units.startswith("p"):
            units = "pounds"
        elif units.startswith("k"):
            units = "kilograms"
        else:
            console.print("Please enter a p or k")
            continue
        break
    return units


def set_loads() -> dict:
    while True:
        units = _get_units()
        console.print("Enter the weight for the...")
        light_load = IntPrompt.ask("Light kettlebell")
        medium_load = IntPrompt.ask("Medium kettlebell")
        heavy_load = IntPrompt.ask("Heavy kettlebell")
        loads = {
            "units": units,
            "light load": light_load,
            "medium load": medium_load,
            "heavy load": heavy_load,
        }
        console.clear()
        for label, value in loads.items():
            console.print(f"{label.title()}: {value}")
        if Confirm.ask(
            "Are these loads correct? If you confirm, they will be used to generate sessions."
        ):
            break
    return loads


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
