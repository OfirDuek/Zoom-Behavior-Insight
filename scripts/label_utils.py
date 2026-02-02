import pandas as pd

LABEL_MAPS = {
    "gaze": {
        "camera": 0,
        "not_camera": 1,
        "not camera": 1,
        "eyes_closed": 2,
        "eyes close": 2,
    },
    "headphones": {
        "with_headphones": 0,
        "with headphones": 0,
        "with_headphone": 0,
        "without_headphones": 1,
        "without headphones": 1,
        "without_headphone": 1,
        "unknown": 2,
    },
    "environment": {"indoor": 0, "outdoor": 1},
    "privacy": {"private": 0, "public": 1},
    "object": {"cup": 0, "phone": 1, "pen": 2, "none": 3, "other": 4, "unknown": 5},
}

NUM_CLASSES = {
    "gaze": 3,
    "headphones": 3,
    "environment": 2,
    "privacy": 2,
    "object": 6,
}

CSV_COLS = {
    "gaze": "Gaze",
    "headphones": "Headphones",
    "environment": "Environment",
    "privacy": "Privacy",
    "object": "ObjectInHand",
}

def clean_label(v):
    if pd.isna(v):
        return ""
    return str(v).strip().lower()