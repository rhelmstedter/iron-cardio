from collections import Counter, namedtuple
from random import choices, choice, seed
from rich import print

Session = namedtuple(
    "Session", ["bells", "intensity", "variation", "constraint", "volume", "load"]
)


def create_ic_session():
    intensity = choices(
        population=["Hard Intensity", "Medium Intensity", "Easy Intensity"],
        weights=[1 / 6, 3 / 6, 2 / 6],
    )[0]
    if intensity == "Hard Intensity":
        variation = choices(
            population=[
                "Classic + Snatch",
                "Traveling 2s",
                "Moving Target",
            ],
            weights=[1 / 3, 1 / 3, 1 / 3],
        )[0]
    elif intensity == "Medium Intensity":
        variation = choices(
            population=["Rep Ladder", "Weight Ladder", "SFG II Focus"],
            weights=[1 / 6, 3 / 6, 2 / 6],
        )[0]
    else:
        variation = "Classic"

    constraint = choices(["work", "time"], [2 / 6, 4 / 6])
    if constraint == "work":
        volume = choices(
            population=["40 sets +", "30 sets", "20 sets"],
            weights=[2 / 6, 2 / 6, 2 / 6],
        )[0]
    else:
        volume = choices(
            population=["40 mins", "30 mins", "20 mins", "10 mins"],
            weights=[1 / 6, 2 / 6, 2 / 6, 1 / 6],
        )[0]
    load = choices(
        population=["heavy load", "medium load", "light load"],
        weights=[2 / 6, 3 / 6, 1 / 6],
    )[0]
    return Session(intensity, variation, constraint, volume, load)


def simulation():
    sessions = [create_ic_session() for s in range(3 * 52)]
    stats = Counter()
    for session in sessions:
        for c in session:
            stats.update([c])
    return stats


if __name__ == "__main__":
    #     session = create_ic_session()
    #     print(f"""Today's Workout
    # ===============
    # Intensity: {session.intensity.title()}
    # Variation: {session.variation}
    # Constraint: {session.constraint.title()}
    # Volume: {session.volume.title()}
    # Load: {session.load.title()}
    # """)
    #
    one_year = simulation()
    one_year = dict(sorted(one_year.items(), key=lambda x: x[1], reverse=True))
    width = len(max(one_year.keys(), key=len))
    for session, count in one_year.items():
        print(f"{session: >{width}}: " + "#" * count)
