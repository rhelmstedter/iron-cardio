import json
import pytest
from typer.testing import CliRunner


from ironcardio import DB_READ_ERROR, SUCCESS, __app_name__, __version__, cli, ironcardio

runner = CliRunner()

test_data1 = {
    "description": ["Clean", "the", "house"],
    "priority": 1,
    "todo": {
        "Description": "Clean the house.",
        "Priority": 1,
        "Done": False,
    },
}
test_data2 = {
    "description": ["Wash the car"],
    "priority": 2,
    "todo": {
        "Description": "Wash the car.",
        "Priority": 2,
        "Done": False,
    },
}


def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout


@pytest.fixture
def mock_json_file(tmp_path):
    sesssion = [
        {
            "bells": "Single Bell",
            "variation": "Classic",
            "time": "20 mins",
            "load": "medium load",
            "swings": "No Swings",
        }
    ]
    db_file = tmp_path / "ironcardio.json"
    with db_file.open("w") as db:
        json.dump(sesssion, db, indent=4)
    return db_file


@pytest.mark.parametrize(
    "description, priority, expected",
    [
        pytest.param(
            test_data1["description"],
            test_data1["priority"],
            (test_data1["todo"], SUCCESS),
        ),
        pytest.param(
            test_data2["description"],
            test_data2["priority"],
            (test_data2["todo"], SUCCESS),
        ),
    ],
)
def test_add(mock_json_file, description, priority, expected):
    todoer = ironcardio.SessionConstructor(mock_json_file)
    assert todoer.add(description, priority) == expected
    read = todoer._db_handler.read_todos()
    assert len(read.todo_list) == 2
