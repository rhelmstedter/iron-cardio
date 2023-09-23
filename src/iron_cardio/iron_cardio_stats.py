def calc_session_stats(session, bodyweight: int) -> dict:
    """Calculate the stats for a given session.
    :param session: The session for which to calculate the stats.
    :param bodyweight: The user's bodyweight at time of the session.
    :returns: A dict containing total weight moved, number of reps, and the pace.
    """
    formulas = {
        "Double Classic": {
            "weight moved": 2 * 3 * session.sets * session.load
            + (session.swings * session.load),
            "reps": 3 * session.sets,
            "pace": (session.time * 60) / (3 * session.sets),
        },
        "Double Classic + Pullup": {
            "weight moved": (
                2 * 3 * session.sets * session.load
                + (session.swings * session.load)
                + bodyweight * session.sets
            ),
            "reps": 4 * session.sets,
            "pace": (session.time * 60) / (4 * session.sets),
        },
        "Double Traveling 2s": {
            "weight moved": 2 * 4 * session.sets * session.load
            + (session.swings * session.load),
            "reps": 4 * session.sets,
            "pace": (session.time * 60) / (4 * session.sets),
        },
        "SFG II Focus": {
            "weight moved": 2 * 3 * session.sets * session.load
            + (session.swings * session.load),
            "reps": 3 * session.sets,
            "pace": (session.time * 60) / (3 * session.sets),
        },
        "Classic": {
            "weight moved": 3 * session.sets * session.load
            + (session.swings * session.load),
            "reps": 3 * session.sets,
            "pace": (session.time * 60) / (3 * session.sets),
        },
        "Classic + Pullup": {
            "weight moved": (
                3 * session.sets * session.load
                + (session.swings * session.load)
                + bodyweight * session.sets // 2
            ),
            "reps": 3 * session.sets + session.sets // 2,
            "pace": (session.time * 60) / (3 * session.sets + session.sets // 2),
        },
        "Classic + Snatch": {
            "weight moved": 4 * session.sets * session.load
            + (session.swings * session.load),
            "reps": 4 * session.sets,
            "pace": (session.time * 60) / (4 * session.sets),
        },
        "Traveling 2s": {
            "weight moved": 4 * session.sets * session.load
            + (session.swings * session.load),
            "reps": 4 * session.sets,
            "pace": (session.time * 60) / (4 * session.sets),
        },
        "Traveling 2s + Snatch": {
            "weight moved": 5 * session.sets * session.load
            + (session.swings * session.load),
            "reps": 5 * session.sets,
            "pace": (session.time * 60) / (5 * session.sets),
        },
        "Traveling 2s + Pullup": {
            "weight moved": (
                4 * session.sets * session.load
                + (session.swings * session.load)
                + bodyweight * session.sets // 2
            ),
            "reps": 3 * session.sets + session.sets // 2,
            "pace": (session.time * 60) / (4 * session.sets + session.sets // 2),
        },
    }
    return formulas[session.variation]


def display_session_stats(session, bodyweight):
    """Prints the stats for a given session."""
    stats = calc_session_stats(session, bodyweight)
    print(
        f"""
Session Stats
=============
    Time: {session.time} mins
    Total Reps: {stats.get("reps")}
    Weight Moved: {stats.get("weight moved"):,} {session.units}
    Pace: {round(stats.get("pace"), 1)} sec/rep"""
    )
