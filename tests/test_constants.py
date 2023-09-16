from iron_cardio.iron_cardio import Session

TEST_SESSION = Session(
    **{
        "bells": "Double Bells",
        "variation": "Double Classic + Pullup",
        "time": "30 mins",
        "load": 28,
        "units": "kilograms",
        "swings": 60,
        "sets": 20,
    }
)

TEST_CACHE_SESSION = Session(
    **{
        "bells": "Double Bells",
        "variation": "Double Classic",
        "time": "20 mins",
        "load": 20,
        "units": "kilograms",
        "swings": False,
        "sets": 0,
    }
)

TEST_DATA = {
    "loads": {
        "units": "kilograms",
        "light load": 20,
        "medium load": 24,
        "heavy load": 28,
    },
    "saved_sessions": [
        {
            "bells": "Double Bells",
            "variation": "Double Classic",
            "time": "20 mins",
            "load": 20,
            "units": "kilograms",
            "swings": False,
            "sets": 29,
        }
    ],
    "cached_sessions": [
        {
            "bells": "Single Bell",
            "variation": "Classic",
            "time": "10 mins",
            "load": 28,
            "units": "kilograms",
            "swings": False,
            "sets": 0,
        },
    ],
}

TEST_DATA_FULL_CACHE = {
    "loads": {
        "units": "kilograms",
        "light load": 20,
        "medium load": 24,
        "heavy load": 28,
    },
    "saved_sessions": [
        {
            "bells": "Double Bells",
            "variation": "Double Classic",
            "time": "20 mins",
            "load": 20,
            "units": "kilograms",
            "swings": False,
            "sets": 29,
        }
    ],
    "cached_sessions": [
        {
            "bells": "Single Bell",
            "variation": "Classic",
            "time": "10 mins",
            "load": 28,
            "units": "kilograms",
            "swings": False,
            "sets": 0,
        },
        {
            "bells": "Double Bells",
            "variation": "Double Classic",
            "time": "10 mins",
            "load": 24,
            "units": "kilograms",
            "swings": False,
            "sets": 0,
        },
        {
            "bells": "Single Bell",
            "variation": "Traveling 2s + Snatch",
            "time": "20 mins",
            "load": 24,
            "units": "kilograms",
            "swings": 70,
            "sets": 0,
        },
        {
            "bells": "Double Bells",
            "variation": "Double Classic",
            "time": "10 mins",
            "load": 28,
            "units": "kilograms",
            "swings": False,
            "sets": 0,
        },
        {
            "bells": "Single Bell",
            "variation": "Traveling 2s + Snatch",
            "time": "20 mins",
            "load": 24,
            "units": "kilograms",
            "swings": False,
            "sets": 0,
        },
        {
            "bells": "Single Bell",
            "variation": "Traveling 2s",
            "time": "20 mins",
            "load": 24,
            "units": "kilograms",
            "swings": 120,
            "sets": 0,
        },
        {
            "bells": "Double Bells",
            "variation": "Double Traveling 2s",
            "time": "30 mins",
            "load": 28,
            "units": "kilograms",
            "swings": 120,
            "sets": 0,
        },
        {
            "bells": "Single Bell",
            "variation": "Traveling 2s + Pullup",
            "time": "30 mins",
            "load": 20,
            "units": "kilograms",
            "swings": False,
            "sets": 0,
        },
        {
            "bells": "Double Bells",
            "variation": "Double Traveling 2s",
            "time": "10 mins",
            "load": 24,
            "units": "kilograms",
            "swings": False,
            "sets": 0,
        },
        {
            "bells": "Double Bells",
            "variation": "Double Classic + Pullup",
            "time": "30 mins",
            "load": 28,
            "units": "kilograms",
            "swings": 60,
            "sets": 0,
        },
    ],
}
