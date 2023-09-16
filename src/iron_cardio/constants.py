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
    "Classic": 1 / 6,
    "Classic + Pullup": 1 / 6,
    "Classic + Snatch": 1 / 6,
    "Traveling 2s": 1 / 6,
    "Traveling 2s + Snatch": 1 / 6,
    "Traveling 2s + Pullup": 1 / 6,
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
