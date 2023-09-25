"""constants for iron cardio session parameters

"""
from pathlib import Path

IRON_CARDIO_HOME = Path().home() / ".iron-cardio"
IRON_CARDIO_DB = IRON_CARDIO_HOME / "iron_cardio_db.json"
BELLS = {"Single Bell": 4 / 6, "Double Bells": 2 / 6}
DOUBLEBELL_VARIATIONS = {
    "Double Classic": 2 / 6,
    "Double Classic + Pullup": 1 / 6,
    "Double Traveling 2s": 2 / 6,
    "SFG II Focus": 1 / 6,
}
SINGLEBELL_VARIATIONS = {
    "Classic": 1 / 7,
    "Classic + Pullup": 1 / 7,
    "Classic + Snatch": 1 / 7,
    "Traveling 2s": 1 / 7,
    "Traveling 2s + Snatch": 1 / 7,
    "Traveling 2s + Pullup": 1 / 7,
    "Single Bell Armor Building Complex": 1 / 7,
}
TIMES = {
    30: 1 / 6,
    20: 4 / 6,
    10: 1 / 6,
}
LOADS = {
    "heavy load": 2 / 6,
    "medium load": 3 / 6,
    "light load": 1 / 6,
}
SWINGS = {True: 2 / 6, False: 4 / 6}
DATE_FORMAT = "%Y-%m-%d"
REP_SCHEMES = {
    "Classic": 3,
    "Classic + Pullup": 3,
    "Double Classic": 3,
    "Double Classic + Pullup": 3,
    "SFG II Focus": 3,
    "Classic + Snatch": 4,
    "Traveling 2s": 4,
    "Traveling 2s + Pullup": 4,
    "Double Traveling 2s": 4,
    "Traveling 2s + Snatch": 5,
    "Single Bell Armor Building Complex": 6,
}
