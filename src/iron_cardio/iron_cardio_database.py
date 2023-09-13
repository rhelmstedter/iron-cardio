import json
import sys
from collections import deque
from dataclasses import asdict
from pathlib import Path

from rich.console import Console
from rich.prompt import IntPrompt

from .constants import IRON_CARDIO_DB
from .iron_cardio import Session

console = Console()


def _database_exists() -> None:
    """Checks to make sure the database exists."""
    if not IRON_CARDIO_DB.is_file():
        console.print("[red]:warning: Could not find Iron Cardio database.")
        console.print(
            "[yellow] Try running [underline]iron-cardio init[/underline] first."
        )
        sys.exit()


def read_database() -> json:
    """Read from the data base."""
    _database_exists()
    with open(IRON_CARDIO_DB) as db:
        data = json.load(db)
    return data


def write_database(data) -> None:
    """Write data to database."""
    with open(IRON_CARDIO_DB, "w") as db:
        json.dump(data, db)


def confirm_loads() -> None:
    """Checks to make sure the loads have been set in the database."""
    data = read_database()
    if not data["loads"]:
        console.print("[red]:warning: Could not find loads in database.")
        console.print(
            "[yellow] Try running [underline]iron-cardio loads[/underline] first."
        )
        sys.exit()


def cache_session(session: Session) -> None:
    """
    Cache last 10 generated sessions.
    :param session: Session object to be stored in the cache
    """
    data = read_database()
    cache = deque(data["cached_sessions"], maxlen=10)
    cache.append(asdict(session))
    data["cached_sessions"] = list(cache)
    write_database(data)


def save_session(session: Session) -> None:
    data = read_database()
    session.sets = IntPrompt.ask("How many sets did you complete?")
    data["saved_sessions"].append(asdict(session))
    write_database(data)


def initialize_database(home: Path, database: Path) -> None:
    """Creates the home directory and the JSON database."""
    home.mkdir()
    data = {"loads": dict(), "saved_sessions": [], "cached_sessions": []}
    write_database(data)
