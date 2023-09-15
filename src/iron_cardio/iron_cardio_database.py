from __future__ import annotations

import json
import shutil
import sys
from collections import deque
from dataclasses import asdict
from pathlib import Path

from rich.console import Console
from rich.prompt import IntPrompt

console = Console()


def _database_exists(db_path: Path) -> None:
    """Checks to make sure the database exists."""
    if not db_path.is_file():
        console.print("[red]:warning: Could not find Iron Cardio database.")
        console.print(
            "[yellow] Try running [underline]iron-cardio init[/underline] first."
        )
        sys.exit()


def read_database(db_path: Path) -> json:
    """Read from the data base."""
    _database_exists(db_path)
    with open(db_path) as db:
        return json.load(db)


def write_database(db_path: Path, data: dict) -> None:
    """Write data to database."""
    with open(db_path, "w") as db:
        json.dump(data, db)


def confirm_loads(db_path: Path) -> None:
    """Checks to make sure the loads have been set in the database."""
    data = read_database(db_path)
    if not data["loads"]:
        console.print("[red]:warning: Could not find loads in database.")
        console.print(
            "[yellow] Try running [underline]iron-cardio loads[/underline] first."
        )
        sys.exit()


def cache_session(db_path: Path, session) -> None:
    """
    Cache last 10 generated sessions.
    :param session: Session object to be stored in the cache
    """
    data = read_database(db_path)
    cache = deque(data["cached_sessions"], maxlen=10)
    cache.append(asdict(session))
    data["cached_sessions"] = list(cache)
    write_database(db_path, data)


def save_session(db_path: Path, session) -> None:
    data = read_database(db_path)
    session.sets = IntPrompt.ask("How many sets did you complete?")
    data["saved_sessions"].append(asdict(session))
    write_database(db_path, data)


def initialize_database(iron_cardio_home: Path, db_path: Path, force: bool) -> None:
    """Creates the home directory and the JSON database."""
    if iron_cardio_home.is_dir() and force:
        shutil.rmtree(iron_cardio_home)
    elif db_path.is_file():
        console.print(
            "[yellow] Database base already exits. Run 'iron-cardio init --force' to overwrite database."
        )
    try:
        iron_cardio_home.mkdir()
    except FileExistsError:
        pass
    data = {"loads": dict(), "saved_sessions": [], "cached_sessions": []}
    write_database(db_path, data)
