from typer.testing import CliRunner


from iron_cardio.__main__ import cli
from iron_cardio.__init__ import __version__

runner = CliRunner()


def test_version():
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert f"{__version__}\n" in result.stdout


def test_create_session():
    result = runner.invoke(cli, ["session"])
    assert result.exit_code == 0
    assert "Today's Session" in result.stdout
