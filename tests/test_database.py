from pathlib import Path
from tempfile import TemporaryDirectory
from iron_cardio.iron_cardio_database import initialize_database

TEST_DATA = {
    "loads": {
        "units": "kilograms",
        "light load": 20,
        "medium load": 24,
        "heavy load": 28,
    },
    "saved_sessions": [
        {
            "bells": "Double Bells",
            "variation": "Double Classic",
            "time": "20 mins",
            "load": 20,
            "units": "kilograms",
            "swings": False,
            "sets": 29,
        }
    ],
    "cached_sessions": [
        {
            "bells": "Single Bell",
            "variation": "Classic",
            "time": "10 mins",
            "load": 28,
            "units": "kilograms",
            "swings": False,
            "sets": 0,
        },
        {
            "bells": "Double Bells",
            "variation": "Double Classic",
            "time": "10 mins",
            "load": 24,
            "units": "kilograms",
            "swings": False,
            "sets": 0,
        },
        {
            "bells": "Single Bell",
            "variation": "Traveling 2s + Snatch",
            "time": "20 mins",
            "load": 24,
            "units": "kilograms",
            "swings": 70,
            "sets": 0,
        },
        {
            "bells": "Double Bells",
            "variation": "Double Classic",
            "time": "10 mins",
            "load": 28,
            "units": "kilograms",
            "swings": False,
            "sets": 0,
        },
        {
            "bells": "Single Bell",
            "variation": "Traveling 2s + Snatch",
            "time": "20 mins",
            "load": 24,
            "units": "kilograms",
            "swings": False,
            "sets": 0,
        },
        {
            "bells": "Single Bell",
            "variation": "Traveling 2s",
            "time": "20 mins",
            "load": 24,
            "units": "kilograms",
            "swings": 120,
            "sets": 0,
        },
        {
            "bells": "Double Bells",
            "variation": "Double Traveling 2s",
            "time": "30 mins",
            "load": 28,
            "units": "kilograms",
            "swings": 120,
            "sets": 0,
        },
        {
            "bells": "Single Bell",
            "variation": "Traveling 2s + Pullup",
            "time": "30 mins",
            "load": 20,
            "units": "kilograms",
            "swings": False,
            "sets": 0,
        },
        {
            "bells": "Double Bells",
            "variation": "Double Traveling 2s",
            "time": "10 mins",
            "load": 24,
            "units": "kilograms",
            "swings": False,
            "sets": 0,
        },
        {
            "bells": "Double Bells",
            "variation": "Double Classic + Pullup",
            "time": "30 mins",
            "load": 28,
            "units": "kilograms",
            "swings": 60,
            "sets": 0,
        },
    ],
}


def test_initalize_database():
    with TemporaryDirectory() as db_dir:
        db_home = Path(db_dir)
        db_file = db_home / "test_db.json"
        initialize_database(db_home, db_file, False)
        assert db_file.is_file()
