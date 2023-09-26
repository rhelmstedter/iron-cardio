from rich import print

from .constants import REP_SCHEMES


def calc_session_stats(session, bodyweight: int) -> dict:
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


def display_session_stats(session, bodyweight):
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
