from iron_cardio.iron_cardio_stats import calc_session_stats, display_session_stats

from .test_constants import (
    TEST_SESSION,
    TEST_SESSION_NO_SWINGS,
    TEST_SESSION_SINGLE_BELL_PULLUPS,
)


def test_display_session_stats():
    actual = calc_session_stats(TEST_SESSION, 90)
    expected = {"weight moved": 6840, "reps": 80, "pace": 22.5}
    assert actual == expected


def test_display_session_stats_no_swings():
    actual = calc_session_stats(TEST_SESSION_NO_SWINGS, 90)
    expected = {"weight moved": 1920, "reps": 80, "pace": 15.0}
    assert actual == expected


def test_display_session_stats_single_bell_pullups(capfd):
    display_session_stats(TEST_SESSION_SINGLE_BELL_PULLUPS, 90)
    output = capfd.readouterr()[0]
    expected = """
Session Stats
=============
    Time: 10 mins
    Total Reps: 35
    Weight Moved: 3,050 kilograms
    Pace: 17.1 sec/rep
"""
    assert expected in output
