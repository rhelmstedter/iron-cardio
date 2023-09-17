import sys
from pathlib import Path
from datetime import date, datetime

import typer
from rich import print
from rich.console import Console
from rich.prompt import Confirm, IntPrompt, Prompt

from . import __version__
from .constants import IRON_CARDIO_DB, IRON_CARDIO_HOME
from .iron_cardio import (
    Session,
    create_custom_session,
    create_session,
    display_session,
    set_loads,
)
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
        iron_cardio_home=IRON_CARDIO_HOME, db_path=IRON_CARDIO_DB, force=force
    )


@cli.command()
def setloads(
    ctx: typer.Context,
) -> None:
    """Set units and loads for iron cardio sessions."""
    loads = set_loads()
    data = read_database(IRON_CARDIO_DB)
    data["loads"] = loads
    write_database(IRON_CARDIO_DB, data)


@cli.command()
def session(
    ctx: typer.Context,
) -> None:
    """Create a random Iron Cardio session."""
    confirm_loads(IRON_CARDIO_DB)
    session = create_session(IRON_CARDIO_DB)
    cache_session(IRON_CARDIO_DB, session)
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
    confirm_loads(IRON_CARDIO_DB)
    if custom:
        session = create_custom_session()
        display_session(session)
    else:
        data = read_database(IRON_CARDIO_DB)
        session = Session(**data["cached_sessions"][-1])
        console.print("Last workout generated:\n")
        display_session(session)
    if Confirm.ask("Save this session?"):
        while True:
            session_date = Prompt.ask(
                "Enter the date of the workout (YYYY-MM-DD), or press enter for today"
            )
            if not session_date:
                session_date = date.today().strftime("%Y-%m-%d")
            try:
                datetime.strptime(session_date, "%Y-%m-%d")
                break
            except ValueError:
                console.print("[yellow]Please enter a valid date[/yellow]")
                continue
        session.sets = IntPrompt.ask("How many sets did you complete?")
        save_session(IRON_CARDIO_DB, session_date, session)


if __name__ == "__main__":
    cli()
