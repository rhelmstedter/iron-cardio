import sys
from pathlib import Path

import typer
from rich import print
from rich.console import Console
from rich.prompt import Confirm, IntPrompt

from . import __version__
from .constants import IRON_CARDIO_DB, IRON_CARDIO_HOME
import iron_cardio.iron_cardio as ic
from .iron_cardio_database import (
    cache_session,
    confirm_loads,
    initialize_database,
    read_database,
    save_session,
    write_database,
)

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
def init(
    ctx: typer.Context,
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        is_flag=True,
        is_eager=True,
    ),
) -> None:
    """Initializes the Iron Cardio database."""
    initialize_database(
        iron_cardio_home=IRON_CARDIO_HOME, database=IRON_CARDIO_DB, force=force
    )


@cli.command()
def loads(
    ctx: typer.Context,
) -> None:
    """Set units and loads for iron cardio sessions."""
    loads = ic.set_loads()
    data = read_database(IRON_CARDIO_DB)
    data["loads"] = loads
    write_database(IRON_CARDIO_DB, data)


@cli.command()
def session(
    ctx: typer.Context,
) -> None:
    """Create a random Iron Cardio session."""
    confirm_loads(IRON_CARDIO_DB)
    session = ic.create_session(IRON_CARDIO_DB)
    cache_session(IRON_CARDIO_DB, session)
    ic.display_session(session)


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
    confirm_loads(IRON_CARDIO_DB)
    if custom:
        session = ic.create_custom_session()
        ic.display_session(session)
    else:
        data = read_database(IRON_CARDIO_DB)
        session = ic.Session(**data["cached_sessions"][-1])
        console.print("Last workout generated:\n")
        ic.display_session(session)
    if Confirm.ask("Save this session?"):
        session.sets = IntPrompt.ask("How many sets did you complete?")
        save_session(IRON_CARDIO_DB, session)


if __name__ == "__main__":
    cli()
