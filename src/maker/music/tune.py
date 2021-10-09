__author__="Aaron Ruen"
import re
from note import Note, NOTES

EASTEREGGS = {
    "Dies Irae": ['G', 'E', 'G', 'F']
    }

# V.3 with bug edits and aestethics
def is_egg_in_tune(egg:list, song:list):
    # .: wild card
    # *: 0 or more
    # .*: O or more of anything
    egg_re = re.compile(".*"+ "".join(egg) + ".*")
    return egg_re.match("".join(song)) is not None


class Tune():
    def __init__(self, tempo=100, base_volume=1, key = "C"):    
        self.mood = None
        self.letter_representation = ['A', 'B', 'C', 'G', 'E', 'G', 'F'] # Note names from Pygame game
        self.notes = []
        self.tempo = tempo # default tempo = 100 because science
        self.base_volume = base_volume # Default 1 (amplitude for square waves)
        self.easter_eggs = self.check_easter_eggs()
        # Run function during init
        self.letter_to_notes()

    def letter_to_notes(self):
        for note in self.letter_representation:          
            self.notes.append(NOTES[note])
        return

    def check_easter_eggs(self):
        print(EASTEREGGS)
        egglist = []
        for key in EASTEREGGS:
            print(EASTEREGGS[key], self.letter_representation)
            print(is_egg_in_tune(EASTEREGGS[key],  self.letter_representation))
            if(is_egg_in_tune(EASTEREGGS[key],  self.letter_representation)):
                egglist.append(key)
        return egglist