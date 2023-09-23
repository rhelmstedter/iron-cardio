from iron_cardio.iron_cardio_stats import calc_session_stats, display_session_stats

from .test_constants import TEST_SESSION, TEST_SESSION_NO_SWINGS


def test_display_session_stats(capfd):
    display_session_stats(TEST_SESSION, 90)
    output = capfd.readouterr()[0]
    expected = """
Session Stats
=============
    Time: 30 mins
    Total Reps: 80
    Weight Moved: 6,840 kilograms
    Pace: 22.5 sec/rep
"""
    assert expected in output


def test_display_session_stats_no_swings(capfd):
    display_session_stats(TEST_SESSION_NO_SWINGS, 90)
    output = capfd.readouterr()[0]
    expected = """
Session Stats
=============
    Time: 20 mins
    Total Reps: 80
    Weight Moved: 1,920 kilograms
    Pace: 15.0 sec/rep
"""
    assert expected in output
