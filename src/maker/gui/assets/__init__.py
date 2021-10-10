"""Assets directory"""

__author__="Tyler Westland"

import os

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))

BACKGROUND_CAT_ASSET = os.path.join(ASSETS_DIR, "background_cat.png")

BACKGROUND_DEAD_CAT_ASSET = os.path.join(ASSETS_DIR, "background_dead_cat.png")

BAR_ASSET = os.path.join(ASSETS_DIR, "bar.png")

BOKEMON_ASSET = os.path.join(ASSETS_DIR, "naruto_pikachu.png")

LIGHTNING_BOLT_ASSET = os.path.join(ASSETS_DIR, "lighting_bolt.png")

NARUTO_ASSET = os.path.join(ASSETS_DIR, "naruto_symbol.png")

PIKACHU_ASSET = os.path.join(ASSETS_DIR, "regular_pikachu.png")

PLAY_BUTTON_ASSET = os.path.join(ASSETS_DIR, "play_button.png")

NOTE_ASSETS = {
        "rest": os.path.join(ASSETS_DIR, "rest.png"),
        "hold": os.path.join(ASSETS_DIR, "hold.png"),
        "G Low": os.path.join(ASSETS_DIR, "G_low.png"),
        "A Low": os.path.join(ASSETS_DIR, "A_low.png"),
        "B Low": os.path.join(ASSETS_DIR, "B_low.png"),
        "C Low": os.path.join(ASSETS_DIR, "C_low.png"),
        "D Low": os.path.join(ASSETS_DIR, "D_low.png"),
        "E Low": os.path.join(ASSETS_DIR, "E_low.png"),
        "F": os.path.join(ASSETS_DIR, "F.png"),
        "G": os.path.join(ASSETS_DIR, "G_high.png"),
        "A": os.path.join(ASSETS_DIR, "A_high.png"),
        "B": os.path.join(ASSETS_DIR, "B_high.png"),
        "C": os.path.join(ASSETS_DIR, "C_high.png"),
        "D": os.path.join(ASSETS_DIR, "D_high.png"),
        "E": os.path.join(ASSETS_DIR, "E_high.png"),
        "wild": os.path.join(ASSETS_DIR, "wild.png"),
        }
