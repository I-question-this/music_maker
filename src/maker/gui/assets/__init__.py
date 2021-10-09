"""Assets directory"""

__author__="Tyler Westland"

import os

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))

NOTE_ASSETS = {
        "A": os.path.join(ASSETS_DIR, "A.png"),
        "B": os.path.join(ASSETS_DIR, "B.png"),
        }
