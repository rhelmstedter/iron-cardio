from collections import Counter, namedtuple
from random import choices, choice
from rich import print

Session = namedtuple("Session", ["bells", "variation", "volume", "load", "swings"])


def create_ic_session():
    bells = choices(
        population=["Single Bell", "Double Bells"],
        weights=[4 / 6, 2 / 6],
    )[0]
    if bells == "Double Bells":
        variation = choices(
            population=[
                "Double Classic",
                "Double Classic + Pullup",
                "Double Traveling 2s",
                "SFG II Focus",
            ],
            weights=[2 / 6, 1 / 6, 2 / 6, 1 / 6],
        )[0]
    elif bells == "Single Bell":
        variation = choices(
            population=[
                "Classic",
                "Classic + Pullup",
                "Classic + Snatch",
                "Traveling 2s",
                "Traveling 2s + Snatch",
            ],
        )[0]
    volume = choices(
        population=["30 mins", "20 mins", "10 mins"],
        weights=[1 / 6, 4 / 6, 1 / 6],
    )[0]
    load = choices(
        population=["heavy load", "medium load", "light load"],
        weights=[2 / 6, 3 / 6, 1 / 6],
    )[0]
    swings = choices(
        population=["Yes", "No Swings"],
        weights=[2 / 6, 4 / 6],
    )[0]
    if swings == "yes":
        swings = choice(range(50, 110, 10))
    return Session(bells, variation, volume, load, swings)


def simulation():
    sessions = [create_ic_session() for s in range(3 * 52)]
    stats = Counter()
    for session in sessions:
        for c in session:
            if isinstance(c, int):
                c = "Swings"
            stats.update([c])
    one_year = dict(sorted(stats.items(), key=lambda x: x[1], reverse=True))
    width = len(max(one_year.keys(), key=len))
    for session, count in one_year.items():
        print(f"{session: >{width}}: " + "#" * count)


if __name__ == "__main__":
    session = create_ic_session()
    if session.swings == "yes":
        swings = f"Swings: {session.swings} reps"
    else:
        swings = ""
    print(f"""Today's Workout
    ===============
    Bells: {session.bells.title()}
    Variation: {session.variation}
    Volume: {session.volume}
    Load: {session.load.title()}
    {swings}
    """)
