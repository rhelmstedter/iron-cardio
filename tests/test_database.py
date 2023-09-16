import json
from pathlib import Path
from tempfile import TemporaryDirectory, NamedTemporaryFile
import pytest

import iron_cardio.iron_cardio_database as ic_db
from .test_constants import TEST_SESSION, TEST_DATA1, TEST_DATA2


@pytest.fixture(scope="function")
def database_home():
    with TemporaryDirectory() as db_dir:
        db_home = Path(db_dir)
        db_path = db_home / "test_db.json"
        return db_path


@pytest.fixture(scope="function")
def database():
    database = NamedTemporaryFile()
    with open(database.name, "w") as db:
        json.dump(TEST_DATA1, db)
    return database


def test_initalize_database(database_home):
    expected = {"loads": dict(), "saved_sessions": [], "cached_sessions": []}
    ic_db.initialize_database(database_home.parents[0], database_home, False)
    assert database_home.is_file()
    assert json.load(open(database_home)) == expected


def test_read_no_database(database_home):
    with pytest.raises(SystemExit):
        ic_db.read_database(database_home)


def test_write_database(database):
    expected = TEST_DATA2
    ic_db.write_database(database.name, TEST_DATA2)
    actual = json.load(open(database.name))
    assert actual == expected


def test_read(database):
    data = ic_db.read_database(Path(database.name))
    assert data == TEST_DATA1


def test_save_session(database):
    ic_db.save_session(Path(database.name), TEST_SESSION)
    data = json.load(open(database.name))
    assert data["saved_sessions"][-1] == {
        "bells": "Double Bells",
        "variation": "Double Classic + Pullup",
        "time": "30 mins",
        "load": 28,
        "units": "kilograms",
        "swings": 60,
        "sets": 20,
    }
