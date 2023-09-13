from pathlib import Path
from tempfile import TemporaryDirectory
from iron_cardio.iron_cardio_database import initialize_database


# def test_initalize_database():
#     with TemporaryDirectory() as db_dir:
#         db_home = Path(db_dir)
#         db_file = db_home / "test_db.json"
#         initialize_database(db_home, db_file)
#         assert db_file.is_file()
