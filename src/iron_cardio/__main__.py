import json
import sys
from pathlib import Path

import typer
from rich import print
from rich.console import Console
from rich.prompt import Confirm, IntPrompt, Prompt

from . import __version__
from .constants import IRON_CARDIO_DB, IRON_CARDIO_HOME
from .iron_cardio import create_ic_session

cli = typer.Typer(add_completion=False)

console = Console()


def report_version(display: bool) -> None:
    """Print version and exit."""
    if display:
        print(f"{Path(sys.argv[0]).name} {__version__}")
        raise typer.Exit()


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
def session(
    ctx: typer.Context,
) -> None:
    """Create a random Iron Cardio session."""
    if not IRON_CARDIO_DB.is_file():
        console.print("[red]:warning: Could not find Iron Cardio database.")
        console.print(
            "[yellow] Try running the [underline]iron-cardio loads[/underline] first."
        )
        sys.exit()

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
    Load: {session.load} {session.units}
    {swings}
    """
    )


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
        data = {"loads": loads, "sessions": []}
        with open(IRON_CARDIO_DB, "w") as db:
            json.dump(data, db)
    else:
        with open(IRON_CARDIO_DB, "r") as db:
            data = json.load(db)
            data["loads"] = loads
        with open(IRON_CARDIO_DB, "w") as db:
            json.dump(data, db)


# TODO when creating a session, first check if the loads have been set
# TODO when saving a session, first check if the database exists.


if __name__ == "__main__":
    cli()
