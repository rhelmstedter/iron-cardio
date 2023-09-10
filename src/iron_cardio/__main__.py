import json
import sys
from collections import deque
from dataclasses import asdict
from pathlib import Path

import typer
from rich import print
from rich.console import Console
from rich.prompt import Confirm, IntPrompt, Prompt

from . import __version__
from .constants import IRON_CARDIO_DB, IRON_CARDIO_HOME
from .iron_cardio import Session, create_session, display_session

cli = typer.Typer(add_completion=False)

console = Console()


def report_version(display: bool) -> None:
    """Print version and exit."""
    if display:
        print(f"{Path(sys.argv[0]).name} {__version__}")
        raise typer.Exit()


def database_exists() -> None:
    if not IRON_CARDIO_DB.is_file():
        console.print("[red]:warning: Could not find Iron Cardio database.")
        console.print(
            "[yellow] Try running the [underline]iron-cardio loads[/underline] first."
        )
        sys.exit()
    return


def cache_session(session: Session) -> None:
    """Cache last 10 generated sessions."""
    with open(IRON_CARDIO_DB) as db:
        data = json.load(db)
        cache = deque(data["cached_sessions"], maxlen=10)
        cache.append(asdict(session))
    with open(IRON_CARDIO_DB, "w") as db:
        data["cached_sessions"] = list(cache)
        json.dump(data, db)


@cli.callback()
def global_options(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        is_flag=True,
        is_eager=True,
        callback=report_version,
    ),
):
    """Create, save, and track progress of Iron Cardio Sessions."""


@cli.command()
def loads(
    ctx: typer.Context,
) -> None:
    """Set units and loads for iron cardio sessions."""
    while True:
        units = Prompt.ask("[P]ounds or [K]ilograms").lower()
        if units.startswith("p"):
            units = "pounds"
        elif units.startswith("k"):
            units = "kilograms"
        else:
            console.print("Please enter a p or k")
            continue
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
    if not IRON_CARDIO_HOME.is_dir():
        IRON_CARDIO_HOME.mkdir()
        data = {"loads": loads, "saved_sessions": [], "cached_sessions": []}
        with open(IRON_CARDIO_DB, "w") as db:
            json.dump(data, db)
    else:
        with open(IRON_CARDIO_DB, "r") as db:
            data = json.load(db)
            data["loads"] = loads
        with open(IRON_CARDIO_DB, "w") as db:
            json.dump(data, db)


@cli.command()
def session(
    ctx: typer.Context,
) -> None:
    """Create a random Iron Cardio session."""
    database_exists()
    session = create_session()
    cache_session(session)
    display_session(session)


@cli.command()
def done(
    custom: bool = typer.Option(
        False,
        "--custom",
        "-c",
        is_flag=True,
        is_eager=True,
    )
) -> None:
    """Save an Iron Cardio session"""
    database_exists()
    # TODO create a way to save a custom session
    # if custom:
    #     save_custom_session()
    with open(IRON_CARDIO_DB, "r") as db:
        data = json.load(db)
        last_workout = dict(**data["cached_sessions"][-1])
    console.print("Last workout generated:")
    display_session(Session(**last_workout))
    if Confirm.ask(
        "Save this workout?"
    ):
        last_workout["sets"] = IntPrompt.ask("How many sets did you complete?")
        data["saved_sessions"].append(last_workout)
        with open(IRON_CARDIO_DB, "w") as db:
            json.dump(data, db)


if __name__ == "__main__":
    cli()
