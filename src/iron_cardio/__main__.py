import typer
import json
import sys
from pathlib import Path
from . import __version__
from .iron_cardio import create_ic_session
from rich import print
from rich.prompt import Prompt, IntPrompt, Confirm

cli = typer.Typer(add_completion=False)


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


@cli.command()
def loads(
    ctx: typer.Context,
) -> None:
    """Set units and loads for iron cardio sessions."""
    while True:
        units = Prompt.ask("[P]ounds or [K]ilograms.").lower()
        if units.startswith("p"):
            units = "pounds"
        elif units.startswith("k"):
            units = "kilograms"
        else:
            print("Please enter a p or k")
            continue
        light_load = IntPrompt.ask("Enter the weight for the light kettlebells:\n> ")
        medium_load = IntPrompt.ask("Enter the weight for the medium kettlebells:\n> ")
        heavy_load = IntPrompt.ask("Enter the weight for the heavy kettlebells:\n> ")
        loads = {"units": units, "light_load": light_load, "medium_load": medium_load, "heavy_load": heavy_load}
        print(loads)
        if Confirm.ask("Are these loads correct? If you confirm, they will be stored under .iron-cardio and used to generate sessions."):
            break

    # data = json.load(open("mydata.json"))
    # json.dump(data, open("mydata.json", "w"))

#TODO when creating a session, first check if the loads have been set
#TODO when saving a session, first check if the database exists.


if __name__ == "__main__":
    cli()
