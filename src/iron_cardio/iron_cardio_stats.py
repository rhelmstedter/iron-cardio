from statistics import mean

import plotext as plt
from rich import print

from .constants import IRON_CARDIO_DB, REP_SCHEMES
from .iron_cardio import Session
from .iron_cardio_database import read_database

MONTH_AND_YEAR = "%m-%y"


def calc_session_stats(session: Session, bodyweight: int) -> dict:
    """Calculate the stats for a given session.
    :param session: The session for which to calculate the stats.
    :param bodyweight: The user's bodyweight at time of the session.
    :returns: A dict containing total weight moved, number of reps, and the pace.
    """
    reps = REP_SCHEMES[session.variation] * session.sets

    if session.bells == "Double Bells":
        load_factor = 2
    else:
        load_factor = 1

    if "Pullup" in session.variation and session.bells == "Double Bells":
        pullup_factor = 1
    elif "Pullup" in session.variation and session.bells == "Single Bell":
        pullup_factor = 0.5
    else:
        pullup_factor = 0

    stats = {
        "weight moved": (
            REP_SCHEMES[session.variation] * session.load * load_factor * session.sets
            + (session.swings * session.load)
            + (bodyweight * int(session.sets * pullup_factor))
        ),
        "reps": reps + int(session.sets * pullup_factor),
        "pace": (session.time * 60) / (reps + (session.sets * pullup_factor)),
    }
    return stats


def display_session_stats(session: Session, bodyweight: int):
    """Prints the stats for a given session."""
    stats = calc_session_stats(session, bodyweight)
    print(
        f"""Session Stats
[green]=============[/green]
Weight Moved: {stats.get("weight moved"):,} {session.units}
  Total Reps: {stats.get("reps")}
        Pace: {round(stats.get("pace"), 1)} sec/rep
    """
    )


def get_all_time_stats(data: dict) -> tuple[list[str], list[int]]:
    """Print stats from all workout in the database.
    :returns: Lists of both dates and weight moved per session.
    """
    bodyweight = data["loads"]["bodyweight"]
    units = data["loads"]["units"]
    dates = []
    stats = []
    sessions = []
    for session_data in data["saved_sessions"]:
        date = session_data["date"]
        session = Session(**session_data["session"])
        dates.append(date)
        stats.append(calc_session_stats(session, bodyweight))
        sessions.append(session)
    total_mins = sum(session.time for session in sessions)
    weight_per_session = [stat["weight moved"] for stat in stats]
    total_weight_moved = sum(weight_per_session)
    total_reps = sum(stat["reps"] for stat in stats)
    average_pace = mean(stat["pace"] for stat in stats)
    print("\nAll Time Stats")
    print("==============")
    print(f"    Total Sessions: {len(stats):,}")
    print(f"        Total Time: {total_mins} mins")
    print(f"Total Weight Moved: {total_weight_moved:,} {units}")
    print(f"        Total Reps: {total_reps:,}")
    print(f"      Average Pace: {average_pace:.1f} sec/rep")
    return dates, weight_per_session


def plot_sessions(dates: list[str], weight_per_session: list[int]) -> None:
    """Plot weight per session."""
    background_color = "yellow"
    foreground_color = "black"
    plt.clear_color()
    plt.date_form("Y-m-d")
    plt.plot(dates, weight_per_session, marker="hd", color=foreground_color)
    plt.ticks_color(foreground_color)
    plt.plotsize(100, 30)
    plt.canvas_color(background_color)
    plt.axes_color(background_color)
    plt.title("Weight Moved Per Session")
    plt.xlabel("Date")
    plt.show()
